#
# Copyright (c) 2023, NVIDIA CORPORATION. All rights reserved.
#
import logging
from typing import List

from aistore.sdk.const import (
    HTTP_METHOD_DELETE,
    ACT_DELETE_OBJECTS,
    ACT_PREFETCH_OBJECTS,
    HTTP_METHOD_POST,
    ACT_EVICT_OBJECTS,
    ACT_COPY_OBJECTS,
    PROVIDER_AIS,
    ACT_TRANSFORM_OBJECTS,
)
from aistore.sdk.etl_const import DEFAULT_ETL_TIMEOUT
from aistore.sdk.multiobj.object_names import ObjectNames
from aistore.sdk.multiobj.object_range import ObjectRange
from aistore.sdk.multiobj.object_template import ObjectTemplate
from aistore.sdk.types import (
    TCMultiObj,
    BucketModel,
    CopyBckMsg,
    TransformBckMsg,
    TCBckMsg,
)


# pylint: disable=unused-variable
class ObjectGroup:
    """
    A class representing multiple objects within the same bucket. Only one of obj_names, obj_range, or obj_template
     should be provided.

    Args:
        bck (Bucket): Bucket the objects belong to
        obj_names (list[str], optional): List of object names to include in this collection
        obj_range (ObjectRange, optional): Range defining which object names in the bucket should be included
        obj_template (str, optional): String argument to pass as template value directly to api
    """

    def __init__(
        self,
        bck,
        obj_names: list = None,
        obj_range: ObjectRange = None,
        obj_template: str = None,
    ):
        self.bck = bck
        num_args = sum(
            1 if x is not None else 0 for x in [obj_names, obj_range, obj_template]
        )
        if num_args != 1:
            raise ValueError(
                "ObjectGroup accepts one and only one of: obj_names, obj_range, or obj_template"
            )
        if obj_range and not isinstance(obj_range, ObjectRange):
            raise TypeError("obj_range must be of type ObjectRange")

        if obj_range:
            self._obj_collection = obj_range
        elif obj_names:
            self._obj_collection = ObjectNames(obj_names)
        else:
            self._obj_collection = ObjectTemplate(obj_template)

    def delete(self):
        """
        Deletes a list or range of objects in a bucket

        Raises:
            aistore.sdk.errors.AISError: All other types of errors with AIStore
            requests.ConnectionError: Connection error
            requests.ConnectionTimeout: Timed out connecting to AIStore
            requests.exceptions.HTTPError: Service unavailable
            requests.RequestException: "There was an ambiguous exception that occurred while handling..."
            requests.ReadTimeout: Timed out receiving response from AIStore

        Returns:
            Job ID (as str) that can be used to check the status of the operation

        """

        return self.bck.make_request(
            HTTP_METHOD_DELETE,
            ACT_DELETE_OBJECTS,
            value=self._obj_collection.get_value(),
        ).text

    def evict(self):
        """
        Evicts a list or range of objects in a bucket so that they are no longer cached in AIS
        NOTE: only Cloud buckets can be evicted.

        Raises:
            aistore.sdk.errors.AISError: All other types of errors with AIStore
            requests.ConnectionError: Connection error
            requests.ConnectionTimeout: Timed out connecting to AIStore
            requests.exceptions.HTTPError: Service unavailable
            requests.RequestException: "There was an ambiguous exception that occurred while handling..."
            requests.ReadTimeout: Timed out receiving response from AIStore

        Returns:
            Job ID (as str) that can be used to check the status of the operation

        """
        self.bck.verify_cloud_bucket()
        return self.bck.make_request(
            HTTP_METHOD_DELETE,
            ACT_EVICT_OBJECTS,
            value=self._obj_collection.get_value(),
        ).text

    def prefetch(self):
        """
        Prefetches a list or range of objects in a bucket so that they are cached in AIS
        NOTE: only Cloud buckets can be prefetched.

        Raises:
            aistore.sdk.errors.AISError: All other types of errors with AIStore
            requests.ConnectionError: Connection error
            requests.ConnectionTimeout: Timed out connecting to AIStore
            requests.exceptions.HTTPError: Service unavailable
            requests.RequestException: "There was an ambiguous exception that occurred while handling..."
            requests.ReadTimeout: Timed out receiving response from AIStore

        Returns:
            Job ID (as str) that can be used to check the status of the operation

        """
        self.bck.verify_cloud_bucket()
        return self.bck.make_request(
            HTTP_METHOD_POST,
            ACT_PREFETCH_OBJECTS,
            value=self._obj_collection.get_value(),
        ).text

    # pylint: disable=too-many-arguments
    def copy(
        self,
        to_bck: str,
        to_provider: str = PROVIDER_AIS,
        prepend: str = "",
        continue_on_error: bool = False,
        dry_run: bool = False,
        force: bool = False,
    ):
        """
        Copies a list or range of objects in a bucket

        Args:
            to_bck (str): Name of the destination bucket
            to_provider (str, optional): Name of destination bucket provider
            prepend (str, optional): Value to prepend to the name of copied objects
            continue_on_error (bool, optional): Whether to continue if there is an error copying a single object
            dry_run (bool, optional): Skip performing the copy and just log the intended actions
            force (bool, optional): Force this job to run over others in case it conflicts
                (see "limited coexistence" and xact/xreg/xreg.go)

        Raises:
            aistore.sdk.errors.AISError: All other types of errors with AIStore
            requests.ConnectionError: Connection error
            requests.ConnectionTimeout: Timed out connecting to AIStore
            requests.exceptions.HTTPError: Service unavailable
            requests.RequestException: "There was an ambiguous exception that occurred while handling..."
            requests.ReadTimeout: Timed out receiving response from AIStore

        Returns:
            Job ID (as str) that can be used to check the status of the operation

        """
        if dry_run:
            logger = logging.getLogger(f"{__name__}.copy")
            logger.info(
                "Copy dry-run. Running with dry_run=False will copy the following objects from bucket '%s' to '%s': %s",
                f"{self.bck.provider}://{self.bck.name}",
                f"{to_provider}://{to_bck}",
                list(self._obj_collection),
            )

        to_bck = BucketModel(name=to_bck, provider=to_provider)
        copy_msg = CopyBckMsg(prepend=prepend, dry_run=dry_run, force=force)
        value = TCMultiObj(
            to_bck=to_bck,
            tc_msg=TCBckMsg(copy_msg=copy_msg),
            object_selection=self._obj_collection.get_value(),
            continue_on_err=continue_on_error,
        ).as_dict()
        return self.bck.make_request(
            HTTP_METHOD_POST, ACT_COPY_OBJECTS, value=value
        ).text

    # pylint: disable=too-many-arguments
    def transform(
        self,
        to_bck: str,
        etl_name: str,
        timeout: str = DEFAULT_ETL_TIMEOUT,
        to_provider: str = PROVIDER_AIS,
        prepend: str = "",
        continue_on_error: bool = False,
        dry_run: bool = False,
        force: bool = False,
    ):
        """
        Performs ETL operation on a list or range of objects in a bucket, placing the results in the destination bucket

        Args:
            to_bck (str): Name of the destination bucket
            etl_name (str): Name of existing ETL to apply
            timeout (str): Timeout of the ETL job (e.g. 5m for 5 minutes)
            to_provider (str, optional): Name of destination bucket provider
            prepend (str, optional): Value to prepend to the name of resulting transformed objects
            continue_on_error (bool, optional): Whether to continue if there is an error transforming a single object
            dry_run (bool, optional): Skip performing the transform and just log the intended actions
            force (bool, optional): Force this job to run over others in case it conflicts
                (see "limited coexistence" and xact/xreg/xreg.go)

        Raises:
            aistore.sdk.errors.AISError: All other types of errors with AIStore
            requests.ConnectionError: Connection error
            requests.ConnectionTimeout: Timed out connecting to AIStore
            requests.exceptions.HTTPError: Service unavailable
            requests.RequestException: "There was an ambiguous exception that occurred while handling..."
            requests.ReadTimeout: Timed out receiving response from AIStore

        Returns:
            Job ID (as str) that can be used to check the status of the operation

        """
        if dry_run:
            logger = logging.getLogger(f"{__name__}.transform")
            logger.info(
                "Transform dry-run. Running with dry_run=False will apply ETL '%s' to objects %s",
                etl_name,
                list(self._obj_collection),
            )

        to_bck = BucketModel(name=to_bck, provider=to_provider)
        copy_msg = CopyBckMsg(prepend=prepend, dry_run=dry_run, force=force)
        transform_msg = TransformBckMsg(etl_name=etl_name, timeout=timeout)
        value = TCMultiObj(
            to_bck=to_bck,
            tc_msg=TCBckMsg(transform_msg=transform_msg, copy_msg=copy_msg),
            object_selection=self._obj_collection.get_value(),
            continue_on_err=continue_on_error,
        ).as_dict()
        return self.bck.make_request(
            HTTP_METHOD_POST, ACT_TRANSFORM_OBJECTS, value=value
        ).text

    def list_names(self) -> List[str]:
        """
        List all the object names included in this group of objects

        Returns:
            List of object names

        """
        return list(self._obj_collection)
