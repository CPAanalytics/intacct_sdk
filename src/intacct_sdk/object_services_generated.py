from __future__ import annotations

from typing import Dict, Iterable, Optional

from .models import QueryResult, ResultData
from .object_services_base import ObjectService


class ObjectServices:
    def __init__(self, session_client) -> None:
        self._session_client = session_client

    def __getattr__(self, name: str) -> ObjectService:
        return ObjectService(self._session_client, name)


class AccttitlebylocService(ObjectService):
    """Service for ACCTTITLEBYLOC."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ACCTTITLEBYLOC")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ACCTTITLEBYLOC records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ACCTTITLEBYLOC records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ACCTTITLEBYLOC.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ACCTTITLEBYLOC.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ACCTTITLEBYLOC.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class AccumulationtypeService(ObjectService):
    """Service for ACCUMULATIONTYPE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ACCUMULATIONTYPE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ACCUMULATIONTYPE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ACCUMULATIONTYPE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ACCUMULATIONTYPE.

Valid fields (from Docs samples):
- NAME"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ACCUMULATIONTYPE.

Valid fields (from Docs samples):
- RECORDNO
- STATUS"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ACCUMULATIONTYPE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class AchbankService(ObjectService):
    """Service for ACHBANK."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ACHBANK")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ACHBANK records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ACHBANK records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ACHBANK.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ACHBANK.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ACHBANK.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ActivitylogService(ObjectService):
    """Service for ACTIVITYLOG."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ACTIVITYLOG")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ACTIVITYLOG records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ACTIVITYLOG records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ACTIVITYLOG.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ACTIVITYLOG.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ACTIVITYLOG.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class AdvaudithistoryService(ObjectService):
    """Service for ADVAUDITHISTORY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ADVAUDITHISTORY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ADVAUDITHISTORY records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ADVAUDITHISTORY records.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ADVAUDITHISTORY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ADVAUDITHISTORY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ADVAUDITHISTORY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class AfrsetupService(ObjectService):
    """Service for AFRSETUP."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "AFRSETUP")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read AFRSETUP records via readByQuery.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read AFRSETUP records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create AFRSETUP.

Valid fields (from Docs samples):
- DISABLEDELETE
- DISABLEEDIT
- DISABLERECLASS"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update AFRSETUP.

Valid fields (from Docs samples):
- DISABLEDELETE"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete AFRSETUP.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class AisleService(ObjectService):
    """Service for AISLE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "AISLE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read AISLE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read AISLE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create AISLE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update AISLE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete AISLE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class AllocationService(ObjectService):
    """Service for ALLOCATION."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ALLOCATION")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ALLOCATION records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ALLOCATION records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ALLOCATION.

Valid fields (from Docs samples):
- ALLOCATIONENTRIES.ALLOCATIONENTRY.CLASSID
- ALLOCATIONENTRIES.ALLOCATIONENTRY.CONTRACTID
- ALLOCATIONENTRIES.ALLOCATIONENTRY.CUSTOMERID
- ALLOCATIONENTRIES.ALLOCATIONENTRY.DEPARTMENTID
- ALLOCATIONENTRIES.ALLOCATIONENTRY.EMPLOYEEID
- ALLOCATIONENTRIES.ALLOCATIONENTRY.ITEMID
- ALLOCATIONENTRIES.ALLOCATIONENTRY.LOCATIONID
- ALLOCATIONENTRIES.ALLOCATIONENTRY.PROJECTID
- ALLOCATIONENTRIES.ALLOCATIONENTRY.VALUE
- ALLOCATIONENTRIES.ALLOCATIONENTRY.VENDORID
- ALLOCATIONENTRIES.ALLOCATIONENTRY.WAREHOUSEID
- ALLOCATIONID
- DESCRIPTION
- DOCNUMBER
- STATUS
- SUPDOCID
- TYPE"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ALLOCATION.

Valid fields (from Docs samples):
- ALLOCATIONENTRIES.ALLOCATIONENTRY.CLASSID
- ALLOCATIONENTRIES.ALLOCATIONENTRY.CONTRACTID
- ALLOCATIONENTRIES.ALLOCATIONENTRY.CUSTOMERID
- ALLOCATIONENTRIES.ALLOCATIONENTRY.DEPARTMENTID
- ALLOCATIONENTRIES.ALLOCATIONENTRY.EMPLOYEEID
- ALLOCATIONENTRIES.ALLOCATIONENTRY.ITEMID
- ALLOCATIONENTRIES.ALLOCATIONENTRY.LOCATIONID
- ALLOCATIONENTRIES.ALLOCATIONENTRY.PROJECTID
- ALLOCATIONENTRIES.ALLOCATIONENTRY.VALUE
- ALLOCATIONENTRIES.ALLOCATIONENTRY.VENDORID
- ALLOCATIONENTRIES.ALLOCATIONENTRY.WAREHOUSEID
- DESCRIPTION
- DOCNUMBER
- RECORDNO
- STATUS
- SUPDOCID
- TYPE"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ALLOCATION.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class AllocationentryService(ObjectService):
    """Service for ALLOCATIONENTRY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ALLOCATIONENTRY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ALLOCATIONENTRY records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ALLOCATIONENTRY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ALLOCATIONENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ALLOCATIONENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ALLOCATIONENTRY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ApaccountlabelService(ObjectService):
    """Service for APACCOUNTLABEL."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "APACCOUNTLABEL")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read APACCOUNTLABEL records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read APACCOUNTLABEL records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create APACCOUNTLABEL.

Valid fields (from Docs samples):
- ACCOUNTLABEL
- DESCRIPTION
- GLACCOUNTNO
- OFFSETGLACCOUNTNO
- STATUS"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update APACCOUNTLABEL.

Valid fields (from Docs samples):
- DESCRIPTION
- GLACCOUNTNO
- OFFSETGLACCOUNTNO
- RECORDNO
- STATUS"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete APACCOUNTLABEL.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ApadjustmentService(ObjectService):
    """Service for APADJUSTMENT."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "APADJUSTMENT")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read APADJUSTMENT records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read APADJUSTMENT records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create APADJUSTMENT.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update APADJUSTMENT.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete APADJUSTMENT.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ApadjustmentitemService(ObjectService):
    """Service for APADJUSTMENTITEM."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "APADJUSTMENTITEM")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read APADJUSTMENTITEM records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read APADJUSTMENTITEM records.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create APADJUSTMENTITEM.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update APADJUSTMENTITEM.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete APADJUSTMENTITEM.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ApbillService(ObjectService):
    """Service for APBILL."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "APBILL")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read APBILL records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read APBILL records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create APBILL.

Valid fields (from Docs samples):
- APBILLITEMS.APBILLITEM.ACCOUNTNO
- APBILLITEMS.APBILLITEM.DEPARTMENTID
- APBILLITEMS.APBILLITEM.ENTRYDESCRIPTION
- APBILLITEMS.APBILLITEM.LOCATIONID
- APBILLITEMS.APBILLITEM.TRX_AMOUNT
- BASECURR
- CURRENCY
- DESCRIPTION
- DOCNUMBER
- ONHOLD
- PAYMENTPRIORITY
- RECORDID
- RECPAYMENTDATE
- SUPDOCID
- TERMNAME
- VENDORID
- WHENCREATED
- WHENDUE
- WHENPOSTED"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update APBILL.

Valid fields (from Docs samples):
- DESCRIPTION
- RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete APBILL.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ApbillbatchService(ObjectService):
    """Service for APBILLBATCH."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "APBILLBATCH")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read APBILLBATCH records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read APBILLBATCH records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create APBILLBATCH.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update APBILLBATCH.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete APBILLBATCH.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ApbillitemService(ObjectService):
    """Service for APBILLITEM."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "APBILLITEM")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read APBILLITEM records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read APBILLITEM records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create APBILLITEM.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update APBILLITEM.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete APBILLITEM.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ApbilljointpayeeService(ObjectService):
    """Service for APBILLJOINTPAYEE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "APBILLJOINTPAYEE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read APBILLJOINTPAYEE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read APBILLJOINTPAYEE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create APBILLJOINTPAYEE.

Valid fields (from Docs samples):
- APBILLKEY
- JOINTPAYEENAME
- JOINTPAYEEPRINTAS"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update APBILLJOINTPAYEE.

Valid fields (from Docs samples):
- JOINTPAYEENAME
- JOINTPAYEEPRINTAS
- RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete APBILLJOINTPAYEE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class AppaymentService(ObjectService):
    """Service for APPAYMENT."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "APPAYMENT")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read APPAYMENT records via readByQuery.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read APPAYMENT records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create APPAYMENT.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update APPAYMENT.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete APPAYMENT.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class AppaymentrequestService(ObjectService):
    """Service for APPAYMENTREQUEST."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "APPAYMENTREQUEST")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read APPAYMENTREQUEST records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read APPAYMENTREQUEST records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create APPAYMENTREQUEST.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update APPAYMENTREQUEST.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete APPAYMENTREQUEST.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class AppymtService(ObjectService):
    """Service for APPYMT."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "APPYMT")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read APPYMT records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read APPYMT records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create APPYMT.

Valid fields (from Docs samples):
- APPYMTDETAILS.APPYMTDETAIL.RECORDKEY
- APPYMTDETAILS.APPYMTDETAIL.TRX_PAYMENTAMOUNT
- FINANCIALENTITY
- PAYMENTDATE
- PAYMENTMETHOD
- VENDORID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update APPYMT.

Valid fields (from Docs samples):
- APPYMTDETAILS.APPYMTDETAIL.ENTRYKEY
- APPYMTDETAILS.APPYMTDETAIL.RECORDKEY
- APPYMTDETAILS.APPYMTDETAIL.TRX_PAYMENTAMOUNT
- RECORDNO
- WHENCREATED"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete APPYMT.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class AppymtdetailService(ObjectService):
    """Service for APPYMTDETAIL."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "APPYMTDETAIL")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read APPYMTDETAIL records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read APPYMTDETAIL records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create APPYMTDETAIL.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update APPYMTDETAIL.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete APPYMTDETAIL.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class AprecurbillService(ObjectService):
    """Service for APRECURBILL."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "APRECURBILL")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read APRECURBILL records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read APRECURBILL records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create APRECURBILL.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update APRECURBILL.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete APRECURBILL.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class AprecurbillentryService(ObjectService):
    """Service for APRECURBILLENTRY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "APRECURBILLENTRY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read APRECURBILLENTRY records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read APRECURBILLENTRY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create APRECURBILLENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update APRECURBILLENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete APRECURBILLENTRY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ApretainagereleaseService(ObjectService):
    """Service for APRETAINAGERELEASE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "APRETAINAGERELEASE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read APRETAINAGERELEASE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read APRETAINAGERELEASE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create APRETAINAGERELEASE.

Valid fields (from Docs samples):
- APRETAINAGERELEASEENTRIES.APRETAINAGERELEASEENTRY.RETAINAGEBILLITEMKEY
- APRETAINAGERELEASEENTRIES.APRETAINAGERELEASEENTRY.RETAINAGEBILLKEY
- APRETAINAGERELEASEENTRIES.APRETAINAGERELEASEENTRY.TRX_AMOUNTRELEASED
- DESCRIPTION
- RELEASEDATE"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update APRETAINAGERELEASE.

Valid fields (from Docs samples):
- APRETAINAGERELEASEENTRIES.APRETAINAGERELEASEENTRY.RETAINAGEINVOICEITEMKEY
- APRETAINAGERELEASEENTRIES.APRETAINAGERELEASEENTRY.RETAINAGEINVOICEKEY
- APRETAINAGERELEASEENTRIES.APRETAINAGERELEASEENTRY.TRX_AMOUNTRELEASED
- RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete APRETAINAGERELEASE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ApretainagereleaseentryService(ObjectService):
    """Service for APRETAINAGERELEASEENTRY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "APRETAINAGERELEASEENTRY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read APRETAINAGERELEASEENTRY records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read APRETAINAGERELEASEENTRY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create APRETAINAGERELEASEENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update APRETAINAGERELEASEENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete APRETAINAGERELEASEENTRY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class AptermService(ObjectService):
    """Service for APTERM."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "APTERM")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read APTERM records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read APTERM records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create APTERM.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update APTERM.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete APTERM.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class AraccountlabelService(ObjectService):
    """Service for ARACCOUNTLABEL."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ARACCOUNTLABEL")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ARACCOUNTLABEL records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ARACCOUNTLABEL records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ARACCOUNTLABEL.

Valid fields (from Docs samples):
- ACCOUNTLABEL
- DESCRIPTION
- GLACCOUNTNO
- OFFSETGLACCOUNTNO
- STATUS"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ARACCOUNTLABEL.

Valid fields (from Docs samples):
- DESCRIPTION
- GLACCOUNTNO
- OFFSETGLACCOUNTNO
- RECORDNO
- STATUS"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ARACCOUNTLABEL.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class AradjustmentService(ObjectService):
    """Service for ARADJUSTMENT."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ARADJUSTMENT")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ARADJUSTMENT records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ARADJUSTMENT records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ARADJUSTMENT.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ARADJUSTMENT.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ARADJUSTMENT.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class AradjustmentitemService(ObjectService):
    """Service for ARADJUSTMENTITEM."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ARADJUSTMENTITEM")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ARADJUSTMENTITEM records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ARADJUSTMENTITEM records.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ARADJUSTMENTITEM.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ARADJUSTMENTITEM.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ARADJUSTMENTITEM.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class AradvanceService(ObjectService):
    """Service for ARADVANCE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ARADVANCE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ARADVANCE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ARADVANCE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ARADVANCE.

Valid fields (from Docs samples):
- ARADVANCEITEMS.ARADVANCEITEM.ACCOUNTLABEL
- ARADVANCEITEMS.ARADVANCEITEM.TRX_AMOUNT
- CUSTOMERID
- PAYMENTDATE
- PAYMENTMETHOD
- RECEIPTDATE
- UNDEPOSITEDACCOUNTNO"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ARADVANCE.

Valid fields (from Docs samples):
- DESCRIPTION
- RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ARADVANCE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ArinvoiceService(ObjectService):
    """Service for ARINVOICE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ARINVOICE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ARINVOICE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ARINVOICE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ARINVOICE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ARINVOICE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ARINVOICE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ArinvoicebatchService(ObjectService):
    """Service for ARINVOICEBATCH."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ARINVOICEBATCH")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ARINVOICEBATCH records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ARINVOICEBATCH records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ARINVOICEBATCH.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ARINVOICEBATCH.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ARINVOICEBATCH.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ArpaymentService(ObjectService):
    """Service for ARPAYMENT."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ARPAYMENT")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ARPAYMENT records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ARPAYMENT records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ARPAYMENT.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ARPAYMENT.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ARPAYMENT.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ArpymtService(ObjectService):
    """Service for ARPYMT."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ARPYMT")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ARPYMT records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ARPYMT records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ARPYMT.

Valid fields (from Docs samples):
- ARPYMTDETAILS.ARPYMTDETAIL.RECORDKEY
- ARPYMTDETAILS.ARPYMTDETAIL.TRX_PAYMENTAMOUNT
- CUSTOMERID
- DOCNUMBER
- FINANCIALENTITY
- PAYMENTDATE
- PAYMENTMETHOD
- RECEIPTDATE"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ARPYMT.

Valid fields (from Docs samples):
- ACTION
- RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ARPYMT.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ArrecurinvoiceService(ObjectService):
    """Service for ARRECURINVOICE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ARRECURINVOICE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ARRECURINVOICE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ARRECURINVOICE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ARRECURINVOICE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ARRECURINVOICE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ARRECURINVOICE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ArrecurinvoiceentryService(ObjectService):
    """Service for ARRECURINVOICEENTRY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ARRECURINVOICEENTRY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ARRECURINVOICEENTRY records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ARRECURINVOICEENTRY records.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ARRECURINVOICEENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ARRECURINVOICEENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ARRECURINVOICEENTRY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ArretainagereleaseService(ObjectService):
    """Service for ARRETAINAGERELEASE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ARRETAINAGERELEASE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ARRETAINAGERELEASE records via readByQuery.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ARRETAINAGERELEASE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ARRETAINAGERELEASE.

Valid fields (from Docs samples):
- ARRETAINAGERELEASEENTRIES.ARRETAINAGERELEASEENTRY.RETAINAGEINVOICEITEMKEY
- ARRETAINAGERELEASEENTRIES.ARRETAINAGERELEASEENTRY.RETAINAGEINVOICEKEY
- ARRETAINAGERELEASEENTRIES.ARRETAINAGERELEASEENTRY.TRX_AMOUNTRELEASED
- DESCRIPTION
- RELEASEDATE"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ARRETAINAGERELEASE.

Valid fields (from Docs samples):
- ARRETAINAGERELEASEENTRIES.ARRETAINAGERELEASEENTRY.RETAINAGEINVOICEITEMKEY
- ARRETAINAGERELEASEENTRIES.ARRETAINAGERELEASEENTRY.RETAINAGEINVOICEKEY
- ARRETAINAGERELEASEENTRIES.ARRETAINAGERELEASEENTRY.TRX_AMOUNTRELEASED
- RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ARRETAINAGERELEASE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ArretainagereleaseentryService(ObjectService):
    """Service for ARRETAINAGERELEASEENTRY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ARRETAINAGERELEASEENTRY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ARRETAINAGERELEASEENTRY records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ARRETAINAGERELEASEENTRY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ARRETAINAGERELEASEENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ARRETAINAGERELEASEENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ARRETAINAGERELEASEENTRY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ArtermService(ObjectService):
    """Service for ARTERM."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ARTERM")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ARTERM records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ARTERM records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ARTERM.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ARTERM.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ARTERM.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class AudithistoryService(ObjectService):
    """Service for AUDITHISTORY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "AUDITHISTORY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read AUDITHISTORY records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read AUDITHISTORY records.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create AUDITHISTORY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update AUDITHISTORY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete AUDITHISTORY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class AvailableinventoryService(ObjectService):
    """Service for AVAILABLEINVENTORY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "AVAILABLEINVENTORY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read AVAILABLEINVENTORY records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read AVAILABLEINVENTORY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create AVAILABLEINVENTORY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update AVAILABLEINVENTORY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete AVAILABLEINVENTORY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class BankacctreconService(ObjectService):
    """Service for BANKACCTRECON."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "BANKACCTRECON")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read BANKACCTRECON records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read BANKACCTRECON records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create BANKACCTRECON.

Valid fields (from Docs samples):
- CUTOFFDATE
- FINANCIALENTITY
- MODE
- STMTENDINGBALANCE
- STMTENDINGDATE"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update BANKACCTRECON.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete BANKACCTRECON.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class BankaccttxnfeedService(ObjectService):
    """Service for BANKACCTTXNFEED."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "BANKACCTTXNFEED")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read BANKACCTTXNFEED records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read BANKACCTTXNFEED records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create BANKACCTTXNFEED.

Valid fields (from Docs samples):
- BANKACCTTXNRECORDS.BANKACCTTXNRECORD.AMOUNT
- BANKACCTTXNRECORDS.BANKACCTTXNRECORD.DESCRIPTION
- BANKACCTTXNRECORDS.BANKACCTTXNRECORD.DOCNO
- BANKACCTTXNRECORDS.BANKACCTTXNRECORD.DOCTYPE
- BANKACCTTXNRECORDS.BANKACCTTXNRECORD.POSTINGDATE
- BANKACCTTXNRECORDS.BANKACCTTXNRECORD.TRANSACTIONTYPE
- FEEDDATE
- FEEDTYPE
- FINANCIALENTITY"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update BANKACCTTXNFEED.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete BANKACCTTXNFEED.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class BankfeeService(ObjectService):
    """Service for BANKFEE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "BANKFEE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read BANKFEE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read BANKFEE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create BANKFEE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update BANKFEE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete BANKFEE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class BankfeeentryService(ObjectService):
    """Service for BANKFEEENTRY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "BANKFEEENTRY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read BANKFEEENTRY records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read BANKFEEENTRY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create BANKFEEENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update BANKFEEENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete BANKFEEENTRY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class BinService(ObjectService):
    """Service for BIN."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "BIN")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read BIN records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read BIN records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create BIN.

Valid fields (from Docs samples):
- AISLEID
- BINDESC
- BINID
- BINSIZEID
- FACEID
- ROWID
- WAREHOUSEID
- ZONEID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update BIN.

Valid fields (from Docs samples):
- BINID
- STATUS"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete BIN.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class BinfaceService(ObjectService):
    """Service for BINFACE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "BINFACE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read BINFACE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read BINFACE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create BINFACE.

Valid fields (from Docs samples):
- FACEDESC
- FACEID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update BINFACE.

Valid fields (from Docs samples):
- FACEDESC
- FACEID"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete BINFACE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class BinsizeService(ObjectService):
    """Service for BINSIZE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "BINSIZE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read BINSIZE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read BINSIZE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create BINSIZE.

Valid fields (from Docs samples):
- SIZEDESC
- SIZEID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update BINSIZE.

Valid fields (from Docs samples):
- BINDESC
- RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete BINSIZE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class CctransactionService(ObjectService):
    """Service for CCTRANSACTION."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CCTRANSACTION")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CCTRANSACTION records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CCTRANSACTION records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CCTRANSACTION.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CCTRANSACTION.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CCTRANSACTION.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class CctransactionentryService(ObjectService):
    """Service for CCTRANSACTIONENTRY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CCTRANSACTIONENTRY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CCTRANSACTIONENTRY records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CCTRANSACTIONENTRY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CCTRANSACTIONENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CCTRANSACTIONENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CCTRANSACTIONENTRY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ChangerequestService(ObjectService):
    """Service for CHANGEREQUEST."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CHANGEREQUEST")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CHANGEREQUEST records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CHANGEREQUEST records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CHANGEREQUEST.

Valid fields (from Docs samples):
- CHANGEREQUESTDATE
- CHANGEREQUESTENTRIES.CHANGEREQUESTENTRY.COST
- CHANGEREQUESTENTRIES.CHANGEREQUESTENTRY.COSTTYPEID
- CHANGEREQUESTENTRIES.CHANGEREQUESTENTRY.PRICE
- CHANGEREQUESTENTRIES.CHANGEREQUESTENTRY.PROJECTID
- CHANGEREQUESTENTRIES.CHANGEREQUESTENTRY.TASKID
- CHANGEREQUESTID
- PROJECTID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CHANGEREQUEST.

Valid fields (from Docs samples):
- CHANGEREQUESTSTATUSNAME
- RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CHANGEREQUEST.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ChangerequestentryService(ObjectService):
    """Service for CHANGEREQUESTENTRY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CHANGEREQUESTENTRY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CHANGEREQUESTENTRY records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CHANGEREQUESTENTRY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CHANGEREQUESTENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CHANGEREQUESTENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CHANGEREQUESTENTRY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ChangerequeststatusService(ObjectService):
    """Service for CHANGEREQUESTSTATUS."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CHANGEREQUESTSTATUS")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CHANGEREQUESTSTATUS records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CHANGEREQUESTSTATUS records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CHANGEREQUESTSTATUS.

Valid fields (from Docs samples):
- NAME
- WFTYPE"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CHANGEREQUESTSTATUS.

Valid fields (from Docs samples):
- RECORDNO
- WFTYPE"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CHANGEREQUESTSTATUS.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ChangerequesttypeService(ObjectService):
    """Service for CHANGEREQUESTTYPE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CHANGEREQUESTTYPE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CHANGEREQUESTTYPE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CHANGEREQUESTTYPE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CHANGEREQUESTTYPE.

Valid fields (from Docs samples):
- NAME"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CHANGEREQUESTTYPE.

Valid fields (from Docs samples):
- RECORDNO
- STATUS"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CHANGEREQUESTTYPE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ChargepayoffService(ObjectService):
    """Service for CHARGEPAYOFF."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CHARGEPAYOFF")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CHARGEPAYOFF records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CHARGEPAYOFF records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CHARGEPAYOFF.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CHARGEPAYOFF.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CHARGEPAYOFF.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ChargepayoffentryService(ObjectService):
    """Service for CHARGEPAYOFFENTRY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CHARGEPAYOFFENTRY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CHARGEPAYOFFENTRY records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CHARGEPAYOFFENTRY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CHARGEPAYOFFENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CHARGEPAYOFFENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CHARGEPAYOFFENTRY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class CheckingaccountService(ObjectService):
    """Service for CHECKINGACCOUNT."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CHECKINGACCOUNT")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CHECKINGACCOUNT records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CHECKINGACCOUNT records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CHECKINGACCOUNT.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CHECKINGACCOUNT.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CHECKINGACCOUNT.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ClassService(ObjectService):
    """Service for CLASS."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CLASS")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CLASS records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CLASS records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CLASS.

Valid fields (from Docs samples):
- CLASSID
- NAME"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CLASS.

Valid fields (from Docs samples):
- NAME
- RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CLASS.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ClassgroupService(ObjectService):
    """Service for CLASSGROUP."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CLASSGROUP")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CLASSGROUP records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CLASSGROUP records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CLASSGROUP.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CLASSGROUP.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CLASSGROUP.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class CogsclosedjeService(ObjectService):
    """Service for COGSCLOSEDJE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "COGSCLOSEDJE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read COGSCLOSEDJE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read COGSCLOSEDJE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create COGSCLOSEDJE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update COGSCLOSEDJE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete COGSCLOSEDJE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class CompliancedefinitionService(ObjectService):
    """Service for COMPLIANCEDEFINITION."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "COMPLIANCEDEFINITION")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read COMPLIANCEDEFINITION records via readByQuery.

Fields (from Docs samples):
- ALLOWNEGATIVELIENWAIVERS
- COMPLIANCEDEFINITIONID
- NAME
- RECORDNO"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read COMPLIANCEDEFINITION records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create COMPLIANCEDEFINITION.

Valid fields (from Docs samples):
- CATEGORY
- COMPDEFENTRIES.VENDTYPENAME
- COMPLIANCEDEFINITIONID
- DESCRIPTION
- GENERATERULE
- NAME
- PAYMENTNOTIFICATION
- TRACKBY
- VALIDATIONRULE"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update COMPLIANCEDEFINITION.

Valid fields (from Docs samples):
- COMPDEFENTRIES.DOCPARID
- COMPLIANCEDEFINITIONID
- MINLIENWAIVERAMOUNT
- MINPRIMARYDOCAMOUNT
- PAYMENTNOTIFICATION"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete COMPLIANCEDEFINITION.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class CompliancerecordService(ObjectService):
    """Service for COMPLIANCERECORD."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "COMPLIANCERECORD")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read COMPLIANCERECORD records via readByQuery.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read COMPLIANCERECORD records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create COMPLIANCERECORD.

Valid fields (from Docs samples):
- COMPLIANCETYPEID
- NAME
- NOTES
- PROJECTID
- VENDORID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update COMPLIANCERECORD.

Valid fields (from Docs samples):
- DESCRIPTION
- NOTES
- PROJECTID
- RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete COMPLIANCERECORD.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class CompliancetypeService(ObjectService):
    """Service for COMPLIANCETYPE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "COMPLIANCETYPE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read COMPLIANCETYPE records via readByQuery.

Fields (from Docs samples):
- COMPLIANCETEMPLATE
- COMPLIANCETYPEID
- FINALCOMPLIANCETEMPLATE
- NAME
- RECORDNO
- STATUS"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read COMPLIANCETYPE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create COMPLIANCETYPE.

Valid fields (from Docs samples):
- COMPLIANCEDEFINITIONID
- COMPLIANCETYPEID
- NAME
- SEQNUMID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update COMPLIANCETYPE.

Valid fields (from Docs samples):
- description
- recordno"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete COMPLIANCETYPE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ContactService(ObjectService):
    """Service for CONTACT."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CONTACT")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CONTACT records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CONTACT records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CONTACT.

Valid fields (from Docs samples):
- CONTACTNAME
- PRINTAS"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CONTACT.

Valid fields (from Docs samples):
- PRINTAS
- RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CONTACT.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ContractService(ObjectService):
    """Service for CONTRACT."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CONTRACT")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CONTRACT records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CONTRACT records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CONTRACT.

Valid fields (from Docs samples):
- BEGINDATE
- BILLINGFREQUENCY
- CONTRACTID
- CURRENCY
- CUSTOMERID
- ENDDATE
- EXCHRATETYPE
- LOCATIONID
- NAME
- TERMNAME"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CONTRACT.

Valid fields (from Docs samples):
- CONTRACTID
- DEPARTMENTID
- NAME"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CONTRACT.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ContractbillingscheduleService(ObjectService):
    """Service for CONTRACTBILLINGSCHEDULE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CONTRACTBILLINGSCHEDULE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CONTRACTBILLINGSCHEDULE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CONTRACTBILLINGSCHEDULE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CONTRACTBILLINGSCHEDULE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CONTRACTBILLINGSCHEDULE.

Valid fields (from Docs samples):
- CONTRACTBILLINGSCHEDULEENTRIES.CONTRACTBILLINGSCHEDULEENTRY.POSTINGDATE
- CONTRACTBILLINGSCHEDULEENTRIES.CONTRACTBILLINGSCHEDULEENTRY.RECORDNO
- RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CONTRACTBILLINGSCHEDULE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ContractbillingscheduleentryService(ObjectService):
    """Service for CONTRACTBILLINGSCHEDULEENTRY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CONTRACTBILLINGSCHEDULEENTRY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CONTRACTBILLINGSCHEDULEENTRY records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CONTRACTBILLINGSCHEDULEENTRY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CONTRACTBILLINGSCHEDULEENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CONTRACTBILLINGSCHEDULEENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CONTRACTBILLINGSCHEDULEENTRY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ContractbillingtemplateService(ObjectService):
    """Service for CONTRACTBILLINGTEMPLATE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CONTRACTBILLINGTEMPLATE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CONTRACTBILLINGTEMPLATE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CONTRACTBILLINGTEMPLATE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CONTRACTBILLINGTEMPLATE.

Valid fields (from Docs samples):
- CONTRACTBILLINGTEMPLATEENTRIES.CONTRACTBILLINGTEMPLATEENTRY.PERCENTBILLED
- CONTRACTBILLINGTEMPLATEENTRIES.CONTRACTBILLINGTEMPLATEENTRY.PERIODOFFSET
- DESCRIPTION
- METHOD
- NAME"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CONTRACTBILLINGTEMPLATE.

Valid fields (from Docs samples):
- DESCRIPTION
- NAME"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CONTRACTBILLINGTEMPLATE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ContractbillingtemplateentryService(ObjectService):
    """Service for CONTRACTBILLINGTEMPLATEENTRY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CONTRACTBILLINGTEMPLATEENTRY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CONTRACTBILLINGTEMPLATEENTRY records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CONTRACTBILLINGTEMPLATEENTRY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CONTRACTBILLINGTEMPLATEENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CONTRACTBILLINGTEMPLATEENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CONTRACTBILLINGTEMPLATEENTRY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ContractdetailService(ObjectService):
    """Service for CONTRACTDETAIL."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CONTRACTDETAIL")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CONTRACTDETAIL records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CONTRACTDETAIL records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CONTRACTDETAIL.

Valid fields (from Docs samples):
- BEGINDATE
- BILLINGMETHOD
- BILLINGOPTIONS
- BILLINGTEMPLATENAME
- CONTRACTID
- ENDDATE
- FLATAMOUNT
- ITEMID
- LOCATIONID
- REVENUETEMPLATENAME"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CONTRACTDETAIL.

Valid fields (from Docs samples):
- DEPARTMENTID
- RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CONTRACTDETAIL.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ContractexpenseService(ObjectService):
    """Service for CONTRACTEXPENSE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CONTRACTEXPENSE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CONTRACTEXPENSE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CONTRACTEXPENSE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CONTRACTEXPENSE.

Valid fields (from Docs samples):
- AMOUNT
- CONTRACTDETAILKEY
- CONTRACTID
- ITEMID
- LOCATIONID
- POSTINGDATE
- TEMPLATENAME"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CONTRACTEXPENSE.

Valid fields (from Docs samples):
- DEPARTMENTID
- RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CONTRACTEXPENSE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class Contractexpense2scheduleService(ObjectService):
    """Service for CONTRACTEXPENSE2SCHEDULE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CONTRACTEXPENSE2SCHEDULE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CONTRACTEXPENSE2SCHEDULE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CONTRACTEXPENSE2SCHEDULE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CONTRACTEXPENSE2SCHEDULE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CONTRACTEXPENSE2SCHEDULE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CONTRACTEXPENSE2SCHEDULE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ContractexpensescheduleService(ObjectService):
    """Service for CONTRACTEXPENSESCHEDULE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CONTRACTEXPENSESCHEDULE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CONTRACTEXPENSESCHEDULE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CONTRACTEXPENSESCHEDULE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CONTRACTEXPENSESCHEDULE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CONTRACTEXPENSESCHEDULE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CONTRACTEXPENSESCHEDULE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ContractexpensetemplateService(ObjectService):
    """Service for CONTRACTEXPENSETEMPLATE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CONTRACTEXPENSETEMPLATE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CONTRACTEXPENSETEMPLATE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CONTRACTEXPENSETEMPLATE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CONTRACTEXPENSETEMPLATE.

Valid fields (from Docs samples):
- DESCRIPTION
- METHOD
- NAME
- POSTINGTYPE"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CONTRACTEXPENSETEMPLATE.

Valid fields (from Docs samples):
- DESCRIPTION
- NAME"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CONTRACTEXPENSETEMPLATE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ContractgroupService(ObjectService):
    """Service for CONTRACTGROUP."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CONTRACTGROUP")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CONTRACTGROUP records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CONTRACTGROUP records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CONTRACTGROUP.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CONTRACTGROUP.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CONTRACTGROUP.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ContractitemprclstentytierService(ObjectService):
    """Service for CONTRACTITEMPRCLSTENTYTIER."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CONTRACTITEMPRCLSTENTYTIER")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CONTRACTITEMPRCLSTENTYTIER records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CONTRACTITEMPRCLSTENTYTIER records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CONTRACTITEMPRCLSTENTYTIER.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CONTRACTITEMPRCLSTENTYTIER.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CONTRACTITEMPRCLSTENTYTIER.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ContractitempricelistService(ObjectService):
    """Service for CONTRACTITEMPRICELIST."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CONTRACTITEMPRICELIST")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CONTRACTITEMPRICELIST records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CONTRACTITEMPRICELIST records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CONTRACTITEMPRICELIST.

Valid fields (from Docs samples):
- CONTRACTITEMPRICELISTENTRIES.CONTRACTITEMPRICELISTENTRY.INCLUDEDUNITS
- CONTRACTITEMPRICELISTENTRIES.CONTRACTITEMPRICELISTENTRY.STARTDATE
- CONTRACTITEMPRICELISTENTRIES.CONTRACTITEMPRICELISTENTRY.VALUE
- CONTRACTITEMPRICELISTENTRIES.CONTRACTITEMPRICELISTENTRY.VARUNITRATE
- CURRENCY
- FLTAMTFREQ
- ITEMID
- ITMPRCLSTTYP
- PRICELISTNAME
- QTYRSTPRD
- VARUNITDIVSR"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CONTRACTITEMPRICELIST.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CONTRACTITEMPRICELIST.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ContractitempricelistentryService(ObjectService):
    """Service for CONTRACTITEMPRICELISTENTRY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CONTRACTITEMPRICELISTENTRY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CONTRACTITEMPRICELISTENTRY records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CONTRACTITEMPRICELISTENTRY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CONTRACTITEMPRICELISTENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CONTRACTITEMPRICELISTENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CONTRACTITEMPRICELISTENTRY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ContractmeabundleService(ObjectService):
    """Service for CONTRACTMEABUNDLE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CONTRACTMEABUNDLE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CONTRACTMEABUNDLE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CONTRACTMEABUNDLE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CONTRACTMEABUNDLE.

Valid fields (from Docs samples):
- ADJUSTMENTPROCESS
- APPLYTOJOURNAL1
- CONTRACTID
- CONTRACTMEABUNDLEENTRIES.CONTRACTMEABUNDLEENTRY.BUNDLENO
- CONTRACTMEABUNDLEENTRIES.CONTRACTMEABUNDLEENTRY.CONTRACTDETAILLINENO
- DESCRIPTION
- EFFECTIVEDATE
- NAME
- TYPE"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CONTRACTMEABUNDLE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CONTRACTMEABUNDLE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ContractmeaitempricelistService(ObjectService):
    """Service for CONTRACTMEAITEMPRICELIST."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CONTRACTMEAITEMPRICELIST")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CONTRACTMEAITEMPRICELIST records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CONTRACTMEAITEMPRICELIST records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CONTRACTMEAITEMPRICELIST.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CONTRACTMEAITEMPRICELIST.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CONTRACTMEAITEMPRICELIST.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ContractmeaitempricelistentryService(ObjectService):
    """Service for CONTRACTMEAITEMPRICELISTENTRY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CONTRACTMEAITEMPRICELISTENTRY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CONTRACTMEAITEMPRICELISTENTRY records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CONTRACTMEAITEMPRICELISTENTRY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CONTRACTMEAITEMPRICELISTENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CONTRACTMEAITEMPRICELISTENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CONTRACTMEAITEMPRICELISTENTRY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ContractmeapricelistService(ObjectService):
    """Service for CONTRACTMEAPRICELIST."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CONTRACTMEAPRICELIST")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CONTRACTMEAPRICELIST records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CONTRACTMEAPRICELIST records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CONTRACTMEAPRICELIST.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CONTRACTMEAPRICELIST.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CONTRACTMEAPRICELIST.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ContractpricelistService(ObjectService):
    """Service for CONTRACTPRICELIST."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CONTRACTPRICELIST")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CONTRACTPRICELIST records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CONTRACTPRICELIST records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CONTRACTPRICELIST.

Valid fields (from Docs samples):
- NAME"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CONTRACTPRICELIST.

Valid fields (from Docs samples):
- DESCRIPTION
- NAME"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CONTRACTPRICELIST.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class Contractrevenue2scheduleService(ObjectService):
    """Service for CONTRACTREVENUE2SCHEDULE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CONTRACTREVENUE2SCHEDULE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CONTRACTREVENUE2SCHEDULE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CONTRACTREVENUE2SCHEDULE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CONTRACTREVENUE2SCHEDULE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CONTRACTREVENUE2SCHEDULE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CONTRACTREVENUE2SCHEDULE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ContractrevenuescheduleService(ObjectService):
    """Service for CONTRACTREVENUESCHEDULE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CONTRACTREVENUESCHEDULE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CONTRACTREVENUESCHEDULE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CONTRACTREVENUESCHEDULE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CONTRACTREVENUESCHEDULE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CONTRACTREVENUESCHEDULE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CONTRACTREVENUESCHEDULE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ContractrevenuetemplateService(ObjectService):
    """Service for CONTRACTREVENUETEMPLATE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CONTRACTREVENUETEMPLATE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CONTRACTREVENUETEMPLATE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CONTRACTREVENUETEMPLATE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CONTRACTREVENUETEMPLATE.

Valid fields (from Docs samples):
- DESCRIPTION
- METHOD
- NAME
- POSTINGTYPE"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CONTRACTREVENUETEMPLATE.

Valid fields (from Docs samples):
- DESCRIPTION
- NAME"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CONTRACTREVENUETEMPLATE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ContracttypeService(ObjectService):
    """Service for CONTRACTTYPE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CONTRACTTYPE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CONTRACTTYPE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CONTRACTTYPE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CONTRACTTYPE.

Valid fields (from Docs samples):
- DESCRIPTION
- NAME
- PARENT.NAME
- STATUS"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CONTRACTTYPE.

Valid fields (from Docs samples):
- RECORDNO
- STATUS"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CONTRACTTYPE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ContractusageService(ObjectService):
    """Service for CONTRACTUSAGE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CONTRACTUSAGE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CONTRACTUSAGE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CONTRACTUSAGE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CONTRACTUSAGE.

Valid fields (from Docs samples):
- CONTRACTID
- CONTRACTLINENO
- QUANTITY
- USAGEDATE"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CONTRACTUSAGE.

Valid fields (from Docs samples):
- QUANTITY
- RECORDNO
- USAGEDATE"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CONTRACTUSAGE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class CosttypeService(ObjectService):
    """Service for COSTTYPE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "COSTTYPE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read COSTTYPE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read COSTTYPE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create COSTTYPE.

Valid fields (from Docs samples):
- ACTUALBEGINDATE
- COSTUNITDESCRIPTION
- DESCRIPTION
- PROJECTID
- STANDARDCOSTTYPEID
- TASKID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update COSTTYPE.

Valid fields (from Docs samples):
- ACTUALBEGINDATE
- RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete COSTTYPE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class CreditcardService(ObjectService):
    """Service for CREDITCARD."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CREDITCARD")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CREDITCARD records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CREDITCARD records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CREDITCARD.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CREDITCARD.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CREDITCARD.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class CreditcardfeeService(ObjectService):
    """Service for CREDITCARDFEE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CREDITCARDFEE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CREDITCARDFEE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CREDITCARDFEE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CREDITCARDFEE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CREDITCARDFEE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CREDITCARDFEE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class CreditcardfeeentryService(ObjectService):
    """Service for CREDITCARDFEEENTRY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CREDITCARDFEEENTRY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CREDITCARDFEEENTRY records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CREDITCARDFEEENTRY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CREDITCARDFEEENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CREDITCARDFEEENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CREDITCARDFEEENTRY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class CustomerService(ObjectService):
    """Service for CUSTOMER."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CUSTOMER")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CUSTOMER records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CUSTOMER records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CUSTOMER.

Valid fields (from Docs samples):
- ARACCOUNT
- ARINVOICEPRINTTEMPLATEID
- BILLTO.CONTACTNAME
- COMMENTS
- CONTACTINFO.CONTACTNAME
- CREDITLIMIT
- CURRENCY
- CUSTMESSAGEID
- CUSTOMERID
- CUSTOMFIELD1
- CUSTTYPE
- DELIVERY_OPTIONS
- DISPLAYCONTACT.CELLPHONE
- DISPLAYCONTACT.COMPANYNAME
- DISPLAYCONTACT.EMAIL1
- DISPLAYCONTACT.EMAIL2
- DISPLAYCONTACT.FAX
- DISPLAYCONTACT.FIRSTNAME
- DISPLAYCONTACT.INITIAL
- DISPLAYCONTACT.LASTNAME
- DISPLAYCONTACT.MAILADDRESS.ADDRESS1
- DISPLAYCONTACT.MAILADDRESS.ADDRESS2
- DISPLAYCONTACT.MAILADDRESS.CITY
- DISPLAYCONTACT.MAILADDRESS.COUNTRY
- DISPLAYCONTACT.MAILADDRESS.STATE
- DISPLAYCONTACT.MAILADDRESS.ZIP
- DISPLAYCONTACT.PAGER
- DISPLAYCONTACT.PHONE1
- DISPLAYCONTACT.PHONE2
- DISPLAYCONTACT.PREFIX
- DISPLAYCONTACT.PRINTAS
- DISPLAYCONTACT.TAXABLE
- DISPLAYCONTACT.TAXGROUP
- DISPLAYCONTACT.TAXSCHEDULE
- DISPLAYCONTACT.TAXSOLUTIONID
- DISPLAYCONTACT.URL1
- DISPLAYCONTACT.URL2
- GLGROUP
- HIDEDISPLAYCONTACT
- NAME
- OBJECTRESTRICTION
- OEADJPRINTTEMPLATEID
- OEINVOICEPRINTTEMPLATEID
- OELISTPRINTTEMPLATEID
- OEORDERPRINTTEMPLATEID
- OEOTHERPRINTTEMPLATEID
- OEQUOTEPRINTTEMPLATEID
- OFFSETGLACCOUNTNO
- ONETIME
- ONHOLD
- PARENTID
- RESALENO
- RESTRICTEDDEPARTMENTS
- RESTRICTEDLOCATIONS
- SHIPPINGMETHOD
- SHIPTO.CONTACTNAME
- STATUS
- SUPDOCID
- TAXID
- TERMNAME
- TERRITORYID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CUSTOMER.

Valid fields (from Docs samples):
- ARACCOUNT
- ARINVOICEPRINTTEMPLATEID
- BILLTO.CONTACTNAME
- COMMENTS
- CONTACTINFO.CONTACTNAME
- CREDITLIMIT
- CURRENCY
- CUSTMESSAGEID
- CUSTOMFIELD1
- CUSTTYPE
- DELIVERY_OPTIONS
- DISPLAYCONTACT.CELLPHONE
- DISPLAYCONTACT.COMPANYNAME
- DISPLAYCONTACT.EMAIL1
- DISPLAYCONTACT.EMAIL2
- DISPLAYCONTACT.FAX
- DISPLAYCONTACT.FIRSTNAME
- DISPLAYCONTACT.INITIAL
- DISPLAYCONTACT.LASTNAME
- DISPLAYCONTACT.MAILADDRESS.ADDRESS1
- DISPLAYCONTACT.MAILADDRESS.ADDRESS2
- DISPLAYCONTACT.MAILADDRESS.CITY
- DISPLAYCONTACT.MAILADDRESS.COUNTRY
- DISPLAYCONTACT.MAILADDRESS.STATE
- DISPLAYCONTACT.MAILADDRESS.ZIP
- DISPLAYCONTACT.PAGER
- DISPLAYCONTACT.PHONE1
- DISPLAYCONTACT.PHONE2
- DISPLAYCONTACT.PREFIX
- DISPLAYCONTACT.PRINTAS
- DISPLAYCONTACT.TAXABLE
- DISPLAYCONTACT.TAXGROUP
- DISPLAYCONTACT.TAXSCHEDULE
- DISPLAYCONTACT.TAXSOLUTIONID
- DISPLAYCONTACT.URL1
- DISPLAYCONTACT.URL2
- GLGROUP
- HIDEDISPLAYCONTACT
- NAME
- OBJECTRESTRICTION
- OEADJPRINTTEMPLATEID
- OEINVOICEPRINTTEMPLATEID
- OELISTPRINTTEMPLATEID
- OEORDERPRINTTEMPLATEID
- OEOTHERPRINTTEMPLATEID
- OEQUOTEPRINTTEMPLATEID
- OFFSETGLACCOUNTNO
- ONETIME
- ONHOLD
- PARENTID
- RECORDNO
- RESALENO
- RESTRICTEDDEPARTMENTS
- RESTRICTEDLOCATIONS
- SHIPPINGMETHOD
- SHIPTO.CONTACTNAME
- STATUS
- SUPDOCID
- TAXID
- TERMNAME
- TERRITORYID"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CUSTOMER.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class CustomeremailtemplateService(ObjectService):
    """Service for CUSTOMEREMAILTEMPLATE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CUSTOMEREMAILTEMPLATE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CUSTOMEREMAILTEMPLATE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CUSTOMEREMAILTEMPLATE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CUSTOMEREMAILTEMPLATE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CUSTOMEREMAILTEMPLATE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CUSTOMEREMAILTEMPLATE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class CustomergroupService(ObjectService):
    """Service for CUSTOMERGROUP."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CUSTOMERGROUP")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CUSTOMERGROUP records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CUSTOMERGROUP records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CUSTOMERGROUP.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CUSTOMERGROUP.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CUSTOMERGROUP.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class CustomervisibilityService(ObjectService):
    """Service for CUSTOMERVISIBILITY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CUSTOMERVISIBILITY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CUSTOMERVISIBILITY records via readByQuery.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CUSTOMERVISIBILITY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CUSTOMERVISIBILITY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CUSTOMERVISIBILITY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CUSTOMERVISIBILITY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class CusttypeService(ObjectService):
    """Service for CUSTTYPE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "CUSTTYPE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read CUSTTYPE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read CUSTTYPE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create CUSTTYPE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update CUSTTYPE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete CUSTTYPE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class DdsjobService(ObjectService):
    """Service for DDSJOB."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "DDSJOB")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read DDSJOB records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read DDSJOB records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create DDSJOB.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update DDSJOB.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete DDSJOB.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class DepartmentService(ObjectService):
    """Service for DEPARTMENT."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "DEPARTMENT")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read DEPARTMENT records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read DEPARTMENT records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create DEPARTMENT.

Valid fields (from Docs samples):
- CUSTTITLE
- DEPARTMENTID
- PARENTID
- STATUS
- SUPERVISORID
- TITLE"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update DEPARTMENT.

Valid fields (from Docs samples):
- CUSTTITLE
- PARENTID
- RECORDNO
- STATUS
- SUPERVISORID
- TITLE"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete DEPARTMENT.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class DepartmentgroupService(ObjectService):
    """Service for DEPARTMENTGROUP."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "DEPARTMENTGROUP")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read DEPARTMENTGROUP records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read DEPARTMENTGROUP records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create DEPARTMENTGROUP.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update DEPARTMENTGROUP.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete DEPARTMENTGROUP.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class DepositService(ObjectService):
    """Service for DEPOSIT."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "DEPOSIT")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read DEPOSIT records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read DEPOSIT records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create DEPOSIT.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update DEPOSIT.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete DEPOSIT.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class DepositentryService(ObjectService):
    """Service for DEPOSITENTRY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "DEPOSITENTRY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read DEPOSITENTRY records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read DEPOSITENTRY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create DEPOSITENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update DEPOSITENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete DEPOSITENTRY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class DunningdefinitionService(ObjectService):
    """Service for DUNNINGDEFINITION."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "DUNNINGDEFINITION")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read DUNNINGDEFINITION records via readByQuery.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read DUNNINGDEFINITION records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create DUNNINGDEFINITION.

Valid fields (from Docs samples):
- CURRENCY
- DUNNINGDEFINITIONID
- EMAILTEMPLATEKEY
- MAXAMOUNT
- MAXDAYS
- MINAMOUNT
- MINDAYS
- NOTICESEQUENCE
- PRINTTEMPLATENAME"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update DUNNINGDEFINITION.

Valid fields (from Docs samples):
- CURRENCY
- DUNNINGDEFINITIONID
- EMAILTEMPLATEKEY
- MAXAMOUNT
- MAXDAYS
- MINAMOUNT
- MINDAYS
- NOTICESEQUENCE
- PRINTTEMPLATENAME
- RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete DUNNINGDEFINITION.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class EarningtypeService(ObjectService):
    """Service for EARNINGTYPE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "EARNINGTYPE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read EARNINGTYPE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read EARNINGTYPE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create EARNINGTYPE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update EARNINGTYPE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete EARNINGTYPE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class EeaccountlabelService(ObjectService):
    """Service for EEACCOUNTLABEL."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "EEACCOUNTLABEL")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read EEACCOUNTLABEL records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read EEACCOUNTLABEL records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create EEACCOUNTLABEL.

Valid fields (from Docs samples):
- ACCOUNTLABEL
- DESCRIPTION
- GLACCOUNTNO
- OFFSETGLACCOUNTNO
- STATUS"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update EEACCOUNTLABEL.

Valid fields (from Docs samples):
- DESCRIPTION
- GLACCOUNTNO
- OFFSETGLACCOUNTNO
- RECORDNO
- STATUS"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete EEACCOUNTLABEL.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class EexpensesService(ObjectService):
    """Service for EEXPENSES."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "EEXPENSES")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read EEXPENSES records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read EEXPENSES records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create EEXPENSES.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update EEXPENSES.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete EEXPENSES.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class EmployeeService(ObjectService):
    """Service for EMPLOYEE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "EMPLOYEE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read EMPLOYEE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read EMPLOYEE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create EMPLOYEE.

Valid fields (from Docs samples):
- PERSONALINFO.CONTACTNAME"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update EMPLOYEE.

Valid fields (from Docs samples):
- RECORDNO
- TITLE"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete EMPLOYEE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class EmployeegroupService(ObjectService):
    """Service for EMPLOYEEGROUP."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "EMPLOYEEGROUP")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read EMPLOYEEGROUP records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read EMPLOYEEGROUP records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create EMPLOYEEGROUP.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update EMPLOYEEGROUP.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete EMPLOYEEGROUP.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class EmployeepositionService(ObjectService):
    """Service for EMPLOYEEPOSITION."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "EMPLOYEEPOSITION")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read EMPLOYEEPOSITION records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read EMPLOYEEPOSITION records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create EMPLOYEEPOSITION.

Valid fields (from Docs samples):
- DESCRIPTION
- NAME
- POSITIONID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update EMPLOYEEPOSITION.

Valid fields (from Docs samples):
- NAME
- RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete EMPLOYEEPOSITION.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class EmployeetypeService(ObjectService):
    """Service for EMPLOYEETYPE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "EMPLOYEETYPE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read EMPLOYEETYPE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read EMPLOYEETYPE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create EMPLOYEETYPE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update EMPLOYEETYPE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete EMPLOYEETYPE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class EppaymentService(ObjectService):
    """Service for EPPAYMENT."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "EPPAYMENT")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read EPPAYMENT records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read EPPAYMENT records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create EPPAYMENT.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update EPPAYMENT.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete EPPAYMENT.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class EppaymentrequestService(ObjectService):
    """Service for EPPAYMENTREQUEST."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "EPPAYMENTREQUEST")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read EPPAYMENTREQUEST records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read EPPAYMENTREQUEST records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create EPPAYMENTREQUEST.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update EPPAYMENTREQUEST.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete EPPAYMENTREQUEST.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ExchangerateService(ObjectService):
    """Service for EXCHANGERATE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "EXCHANGERATE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read EXCHANGERATE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read EXCHANGERATE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create EXCHANGERATE.

Valid fields (from Docs samples):
- EXCHANGERATEENTRIES.EXCHANGERATEENTRY.EFFECTIVE_START_DATE
- EXCHANGERATEENTRIES.EXCHANGERATEENTRY.EXCHANGE_RATE
- EXCHANGERATEENTRIES.EXCHANGERATEENTRY.RECIPROCAL_RATE
- FROM_CURRENCY
- TO_CURRENCY
- TYPENAME"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update EXCHANGERATE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete EXCHANGERATE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ExchangerateentryService(ObjectService):
    """Service for EXCHANGERATEENTRY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "EXCHANGERATEENTRY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read EXCHANGERATEENTRY records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read EXCHANGERATEENTRY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create EXCHANGERATEENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update EXCHANGERATEENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete EXCHANGERATEENTRY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ExchangeratetypesService(ObjectService):
    """Service for EXCHANGERATETYPES."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "EXCHANGERATETYPES")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read EXCHANGERATETYPES records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read EXCHANGERATETYPES records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create EXCHANGERATETYPES.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update EXCHANGERATETYPES.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete EXCHANGERATETYPES.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ExpenseadjustmentsService(ObjectService):
    """Service for EXPENSEADJUSTMENTS."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "EXPENSEADJUSTMENTS")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read EXPENSEADJUSTMENTS records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read EXPENSEADJUSTMENTS records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create EXPENSEADJUSTMENTS.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update EXPENSEADJUSTMENTS.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete EXPENSEADJUSTMENTS.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ExpenseadjustmentsitemService(ObjectService):
    """Service for EXPENSEADJUSTMENTSITEM."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "EXPENSEADJUSTMENTSITEM")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read EXPENSEADJUSTMENTSITEM records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read EXPENSEADJUSTMENTSITEM records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create EXPENSEADJUSTMENTSITEM.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update EXPENSEADJUSTMENTSITEM.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete EXPENSEADJUSTMENTSITEM.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ExpensepaymenttypeService(ObjectService):
    """Service for EXPENSEPAYMENTTYPE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "EXPENSEPAYMENTTYPE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read EXPENSEPAYMENTTYPE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read EXPENSEPAYMENTTYPE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create EXPENSEPAYMENTTYPE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update EXPENSEPAYMENTTYPE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete EXPENSEPAYMENTTYPE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class FundstransferService(ObjectService):
    """Service for FUNDSTRANSFER."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "FUNDSTRANSFER")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read FUNDSTRANSFER records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read FUNDSTRANSFER records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create FUNDSTRANSFER.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update FUNDSTRANSFER.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete FUNDSTRANSFER.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class FundstransferentryService(ObjectService):
    """Service for FUNDSTRANSFERENTRY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "FUNDSTRANSFERENTRY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read FUNDSTRANSFERENTRY records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read FUNDSTRANSFERENTRY records.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create FUNDSTRANSFERENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update FUNDSTRANSFERENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete FUNDSTRANSFERENTRY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class GcbookService(ObjectService):
    """Service for GCBOOK."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "GCBOOK")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read GCBOOK records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read GCBOOK records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create GCBOOK.

Valid fields (from Docs samples):
- AUTOELIMINATION
- BOOKID
- BOOKJOURNALSYMBOL
- BOOKJOURNALTITLE
- BOOKSTATJOURNALSYMBOL
- BOOKSTATJOURNALTITLE
- BSTRANMETHOD
- CTANETASSETACCOUNTNO
- CTANETINCOMEACCOUNTNO
- CURRENCY
- DESCRIPTION
- DIMENSIONS
- EENAME
- ISTRANMETHOD
- SOURCEBOOKID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update GCBOOK.

Valid fields (from Docs samples):
- BOOKID
- BUDGETID
- DESCRIPTION"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete GCBOOK.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class GcbookacctratetypeService(ObjectService):
    """Service for GCBOOKACCTRATETYPE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "GCBOOKACCTRATETYPE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read GCBOOKACCTRATETYPE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read GCBOOKACCTRATETYPE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create GCBOOKACCTRATETYPE.

Valid fields (from Docs samples):
- BOOKID
- GLACCOUNTNO
- GLACCTRATETYPES
- OVERRIDERATE"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update GCBOOKACCTRATETYPE.

Valid fields (from Docs samples):
- GCBOOKACCTRATETYPE.GLACCOUNTNO
- GCBOOKACCTRATETYPE.GLACCTRATETYPES
- GCBOOKACCTRATETYPE.OVERRIDEEXPIRYDATE
- GCBOOKACCTRATETYPE.OVERRIDERATE
- GCBOOKACCTRATETYPE.RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete GCBOOKACCTRATETYPE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class GcbookadjjournalService(ObjectService):
    """Service for GCBOOKADJJOURNAL."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "GCBOOKADJJOURNAL")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read GCBOOKADJJOURNAL records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read GCBOOKADJJOURNAL records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create GCBOOKADJJOURNAL.

Valid fields (from Docs samples):
- BOOKID
- BOOKTYPE
- SYMBOL
- TITLE"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update GCBOOKADJJOURNAL.

Valid fields (from Docs samples):
- RECORDNO
- TITLE"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete GCBOOKADJJOURNAL.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class GcbookelimaccountService(ObjectService):
    """Service for GCBOOKELIMACCOUNT."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "GCBOOKELIMACCOUNT")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read GCBOOKELIMACCOUNT records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read GCBOOKELIMACCOUNT records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create GCBOOKELIMACCOUNT.

Valid fields (from Docs samples):
- BOOKID
- GLACCOUNTNO"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update GCBOOKELIMACCOUNT.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete GCBOOKELIMACCOUNT.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class GcbookentityService(ObjectService):
    """Service for GCBOOKENTITY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "GCBOOKENTITY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read GCBOOKENTITY records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read GCBOOKENTITY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create GCBOOKENTITY.

Valid fields (from Docs samples):
- BOOKID
- LOCATIONID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update GCBOOKENTITY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete GCBOOKENTITY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class GcownershipchildentityService(ObjectService):
    """Service for GCOWNERSHIPCHILDENTITY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "GCOWNERSHIPCHILDENTITY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read GCOWNERSHIPCHILDENTITY records via readByQuery.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read GCOWNERSHIPCHILDENTITY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create GCOWNERSHIPCHILDENTITY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update GCOWNERSHIPCHILDENTITY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete GCOWNERSHIPCHILDENTITY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class GcownershipentityService(ObjectService):
    """Service for GCOWNERSHIPENTITY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "GCOWNERSHIPENTITY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read GCOWNERSHIPENTITY records via readByQuery.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read GCOWNERSHIPENTITY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create GCOWNERSHIPENTITY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update GCOWNERSHIPENTITY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete GCOWNERSHIPENTITY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class GcownershipstructureService(ObjectService):
    """Service for GCOWNERSHIPSTRUCTURE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "GCOWNERSHIPSTRUCTURE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read GCOWNERSHIPSTRUCTURE records via readByQuery.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read GCOWNERSHIPSTRUCTURE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create GCOWNERSHIPSTRUCTURE.

Valid fields (from Docs samples):
- AUTOELIMINATION
- DESCRIPTION
- SOURCEBOOKID
- STATUS
- STRUCTURENAME"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update GCOWNERSHIPSTRUCTURE.

Valid fields (from Docs samples):
- DESCRIPTION
- RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete GCOWNERSHIPSTRUCTURE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class GcownershipstructuredetailService(ObjectService):
    """Service for GCOWNERSHIPSTRUCTUREDETAIL."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "GCOWNERSHIPSTRUCTUREDETAIL")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read GCOWNERSHIPSTRUCTUREDETAIL records via readByQuery.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read GCOWNERSHIPSTRUCTUREDETAIL records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create GCOWNERSHIPSTRUCTUREDETAIL.

Valid fields (from Docs samples):
- FROMPERIOD
- GCOWNERSHIPENTITIES.GCOWNERSHIPENTITY.BOOK.BOOKDESCRIPTION
- GCOWNERSHIPENTITIES.GCOWNERSHIPENTITY.BOOK.BOOKID
- GCOWNERSHIPENTITIES.GCOWNERSHIPENTITY.BOOK.BOOKJOURNALSYMBOL
- GCOWNERSHIPENTITIES.GCOWNERSHIPENTITY.BOOK.BOOKJOURNALTITLE
- GCOWNERSHIPENTITIES.GCOWNERSHIPENTITY.BOOK.BOOKSTATJOURNALSYMBOL
- GCOWNERSHIPENTITIES.GCOWNERSHIPENTITY.BOOK.BOOKSTATJOURNALTITLE
- GCOWNERSHIPENTITIES.GCOWNERSHIPENTITY.BOOK.BSTRANMETHOD
- GCOWNERSHIPENTITIES.GCOWNERSHIPENTITY.BOOK.CTANETASSETACCOUNTNO
- GCOWNERSHIPENTITIES.GCOWNERSHIPENTITY.BOOK.CTANETINCOMEACCOUNTNO
- GCOWNERSHIPENTITIES.GCOWNERSHIPENTITY.BOOK.CURRENCY
- GCOWNERSHIPENTITIES.GCOWNERSHIPENTITY.BOOK.EENAME
- GCOWNERSHIPENTITIES.GCOWNERSHIPENTITY.BOOK.ELIMINATIONADJACCT
- GCOWNERSHIPENTITIES.GCOWNERSHIPENTITY.BOOK.ISTRANMETHOD
- GCOWNERSHIPENTITIES.GCOWNERSHIPENTITY.GCOWNERSHIPCHILDENTITIES.GCOWNERSHIPCHILDENTITY.ENTITYID
- GCOWNERSHIPENTITIES.GCOWNERSHIPENTITY.GCOWNERSHIPCHILDENTITIES.GCOWNERSHIPCHILDENTITY.OWNERSHIPPERCENTAGE
- GCOWNERSHIPENTITIES.GCOWNERSHIPENTITY.PARENTENTITYID
- STATE
- STRUCTURENAME"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update GCOWNERSHIPSTRUCTUREDETAIL.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete GCOWNERSHIPSTRUCTUREDETAIL.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class GeninvoicepolicyService(ObjectService):
    """Service for GENINVOICEPOLICY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "GENINVOICEPOLICY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read GENINVOICEPOLICY records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read GENINVOICEPOLICY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create GENINVOICEPOLICY.

Valid fields (from Docs samples):
- CONTRACTID
- INCLUDECONTRACTS
- INCLUDECONTRACTUSAGE
- NAME"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update GENINVOICEPOLICY.

Valid fields (from Docs samples):
- CONTRACTID
- INCLUDECONTRACTS
- RECORDNO
- SCHEDULED"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete GENINVOICEPOLICY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class GeninvoicepreviewService(ObjectService):
    """Service for GENINVOICEPREVIEW."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "GENINVOICEPREVIEW")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read GENINVOICEPREVIEW records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read GENINVOICEPREVIEW records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create GENINVOICEPREVIEW.

Valid fields (from Docs samples):
- ASOFDATE
- DOCPARID
- GLPOSTDATE
- INCLUDECONTRACTS
- INCLUDECONTRACTUSAGE
- INVOICEBY
- INVOICEDATE"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update GENINVOICEPREVIEW.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete GENINVOICEPREVIEW.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class GeninvoicepreviewlineService(ObjectService):
    """Service for GENINVOICEPREVIEWLINE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "GENINVOICEPREVIEWLINE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read GENINVOICEPREVIEWLINE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read GENINVOICEPREVIEWLINE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create GENINVOICEPREVIEWLINE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update GENINVOICEPREVIEWLINE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete GENINVOICEPREVIEWLINE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class GeninvoicerunService(ObjectService):
    """Service for GENINVOICERUN."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "GENINVOICERUN")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read GENINVOICERUN records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read GENINVOICERUN records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create GENINVOICERUN.

Valid fields (from Docs samples):
- PREVIEWKEY"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update GENINVOICERUN.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete GENINVOICERUN.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class GlaccountService(ObjectService):
    """Service for GLACCOUNT."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "GLACCOUNT")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read GLACCOUNT records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read GLACCOUNT records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create GLACCOUNT.

Valid fields (from Docs samples):
- ACCOUNTNO
- TITLE"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update GLACCOUNT.

Valid fields (from Docs samples):
- RECORDNO
- TITLE"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete GLACCOUNT.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class GlaccountbalanceService(ObjectService):
    """Service for GLACCOUNTBALANCE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "GLACCOUNTBALANCE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read GLACCOUNTBALANCE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read GLACCOUNTBALANCE records.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create GLACCOUNTBALANCE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update GLACCOUNTBALANCE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete GLACCOUNTBALANCE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class GlacctallocationService(ObjectService):
    """Service for GLACCTALLOCATION."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "GLACCTALLOCATION")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read GLACCTALLOCATION records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read GLACCTALLOCATION records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create GLACCTALLOCATION.

Valid fields (from Docs samples):
- ACCTALLOCATIONID
- DESCRIPTION
- FOCUSDEPARTMENT
- FOCUSLOCATION
- FOCUSPROJECT
- GLACCTALLOCATIONBASIS.ACCUMULATION
- GLACCTALLOCATIONBASIS.ALLOCATIONMETHOD
- GLACCTALLOCATIONBASIS.GLACCTGRP
- GLACCTALLOCATIONBASIS.LOCNO
- GLACCTALLOCATIONBASIS.REPORTINGBOOK
- GLACCTALLOCATIONBASIS.SKIPNEGATIVE
- GLACCTALLOCATIONBASIS.TIMEPERIOD
- GLACCTALLOCATIONREVERSE.USESOURCEACCOUNT
- GLACCTALLOCATIONSOURCE.GLACCTALLOCATIONSOURCEADJBOOKS.GLACCTALLOCATIONSOURCEADJBOOK.ADJBOOKID
- GLACCTALLOCATIONSOURCE.GLACCTGRP
- GLACCTALLOCATIONSOURCE.LOCNO
- GLACCTALLOCATIONSOURCE.PERCENT2ALLOCATE
- GLACCTALLOCATIONSOURCE.REPORTINGBOOK
- GLACCTALLOCATIONSOURCE.SOURCEINCLUDEREPORTINGBOOK
- GLACCTALLOCATIONSOURCE.TIMEPERIOD
- GLACCTALLOCATIONTARGET.GLACCOUNTNO
- GLACCTALLOCATIONTARGET.JOURNALSYMBOL
- GLACCTALLOCATIONTARGET.REPORTINGBOOK
- METHODOLOGY"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update GLACCTALLOCATION.

Valid fields (from Docs samples):
- GLACCTALLOCATIONBASIS.SKIPNEGATIVE
- RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete GLACCTALLOCATION.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class GlacctallocationgrpService(ObjectService):
    """Service for GLACCTALLOCATIONGRP."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "GLACCTALLOCATIONGRP")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read GLACCTALLOCATIONGRP records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read GLACCTALLOCATIONGRP records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create GLACCTALLOCATIONGRP.

Valid fields (from Docs samples):
- DESCRIPTION
- GLACCTALLOCATIONGRPMEMBERS.GLACCTALLOCATIONGRPMEMBER.GLACCTALLOCATIONID
- GRPERRORPROCESSINGMETHOD
- NAME"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update GLACCTALLOCATIONGRP.

Valid fields (from Docs samples):
- GLACCTALLOCATIONGRPMEMBERS.GLACCTALLOCATIONGRPMEMBER.GLACCTALLOCATIONID
- RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete GLACCTALLOCATIONGRP.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class GlacctallocationrunService(ObjectService):
    """Service for GLACCTALLOCATIONRUN."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "GLACCTALLOCATIONRUN")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read GLACCTALLOCATIONRUN records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read GLACCTALLOCATIONRUN records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create GLACCTALLOCATIONRUN.

Valid fields (from Docs samples):
- ASOFDATE
- EMAIL
- GLACCTALLOCATION
- GLPOSTINGDATE"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update GLACCTALLOCATIONRUN.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete GLACCTALLOCATIONRUN.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class GlacctgrpService(ObjectService):
    """Service for GLACCTGRP."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "GLACCTGRP")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read GLACCTGRP records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read GLACCTGRP records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create GLACCTGRP.

Valid fields (from Docs samples):
- ASOF
- CLASSID
- CUSTOMERID
- DBCR
- DEPTNO
- EMPLOYEEID
- FILTERCLASS
- FILTERCUSTOMER
- FILTERDEPT
- FILTEREMPLOYEE
- FILTERITEM
- FILTERLOC
- FILTERPROJECT
- FILTERVENDOR
- GLACCTRANGES.ACCTRANGE.RANGEFROM
- GLACCTRANGES.ACCTRANGE.RANGETO
- ISKPI
- ITEMID
- LOCNO
- MEMBERTYPE
- NAME
- NORMAL_BALANCE
- PROJECTID
- TITLE
- TOTALTITLE
- VENDORID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update GLACCTGRP.

Valid fields (from Docs samples):
- GLACCTRANGES.ACCTRANGE.RANGEFROM
- GLACCTRANGES.ACCTRANGE.RANGETO
- RECORDNO
- TITLE
- TOTALTITLE"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete GLACCTGRP.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class GlacctgrphierarchyService(ObjectService):
    """Service for GLACCTGRPHIERARCHY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "GLACCTGRPHIERARCHY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read GLACCTGRPHIERARCHY records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read GLACCTGRPHIERARCHY records.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create GLACCTGRPHIERARCHY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update GLACCTGRPHIERARCHY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete GLACCTGRPHIERARCHY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class GlacctgrppurposeService(ObjectService):
    """Service for GLACCTGRPPURPOSE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "GLACCTGRPPURPOSE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read GLACCTGRPPURPOSE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read GLACCTGRPPURPOSE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create GLACCTGRPPURPOSE.

Valid fields (from Docs samples):
- NAME"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update GLACCTGRPPURPOSE.

Valid fields (from Docs samples):
- RECORDNO
- STATUS"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete GLACCTGRPPURPOSE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class GlbatchService(ObjectService):
    """Service for GLBATCH."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "GLBATCH")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read GLBATCH records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read GLBATCH records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create GLBATCH.

Valid fields (from Docs samples):
- BATCH_DATE
- BATCH_TITLE
- ENTRIES.GLENTRY.ACCOUNTNO
- ENTRIES.GLENTRY.AMOUNT
- ENTRIES.GLENTRY.CURRENCY
- ENTRIES.GLENTRY.DEPARTMENT
- ENTRIES.GLENTRY.DESCRIPTION
- ENTRIES.GLENTRY.EXCH_RATE_TYPE_ID
- ENTRIES.GLENTRY.LOCATION
- ENTRIES.GLENTRY.TR_TYPE
- JOURNAL
- REVERSEDATE"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update GLBATCH.

Valid fields (from Docs samples):
- BATCH_DATE
- BATCH_TITLE
- ENTRIES.GLENTRY.ACCOUNTNO
- ENTRIES.GLENTRY.AMOUNT
- ENTRIES.GLENTRY.CURRENCY
- ENTRIES.GLENTRY.DEPARTMENT
- ENTRIES.GLENTRY.DESCRIPTION
- ENTRIES.GLENTRY.EXCH_RATE_TYPE_ID
- ENTRIES.GLENTRY.LOCATION
- ENTRIES.GLENTRY.TR_TYPE
- JOURNAL
- RECORDNO
- REVERSEDATE"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete GLBATCH.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class GlbudgetheaderService(ObjectService):
    """Service for GLBUDGETHEADER."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "GLBUDGETHEADER")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read GLBUDGETHEADER records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read GLBUDGETHEADER records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create GLBUDGETHEADER.

Valid fields (from Docs samples):
- BUDGETID
- DEFAULT_BUDGET
- DESCRIPTION
- GLBUDGETITEMS.GLBUDGETITEM.ACCT_NO
- GLBUDGETITEMS.GLBUDGETITEM.AMOUNT
- GLBUDGETITEMS.GLBUDGETITEM.DEPT_NO
- GLBUDGETITEMS.GLBUDGETITEM.LOCATION_NO
- GLBUDGETITEMS.GLBUDGETITEM.PERIODNAME"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update GLBUDGETHEADER.

Valid fields (from Docs samples):
- GLBUDGETITEMS.GLBUDGETITEM.ACCT_NO
- GLBUDGETITEMS.GLBUDGETITEM.AMOUNT
- GLBUDGETITEMS.GLBUDGETITEM.DEPT_NO
- GLBUDGETITEMS.GLBUDGETITEM.LOCATION_NO
- GLBUDGETITEMS.GLBUDGETITEM.PERIODNAME
- GLBUDGETITEMS.GLBUDGETITEM.RECORDNO
- RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete GLBUDGETHEADER.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class GlbudgetitemService(ObjectService):
    """Service for GLBUDGETITEM."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "GLBUDGETITEM")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read GLBUDGETITEM records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read GLBUDGETITEM records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create GLBUDGETITEM.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update GLBUDGETITEM.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete GLBUDGETITEM.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class GldetailService(ObjectService):
    """Service for GLDETAIL."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "GLDETAIL")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read GLDETAIL records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read GLDETAIL records.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create GLDETAIL.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update GLDETAIL.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete GLDETAIL.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class GlentryService(ObjectService):
    """Service for GLENTRY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "GLENTRY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read GLENTRY records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read GLENTRY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create GLENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update GLENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete GLENTRY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class IccyclecountService(ObjectService):
    """Service for ICCYCLECOUNT."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ICCYCLECOUNT")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ICCYCLECOUNT records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ICCYCLECOUNT records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ICCYCLECOUNT.

Valid fields (from Docs samples):
- CYCLECOUNTDESC
- EMPUSERID
- SHOWQTYONHAND
- WAREHOUSEID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ICCYCLECOUNT.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ICCYCLECOUNT.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class IccyclecountentryService(ObjectService):
    """Service for ICCYCLECOUNTENTRY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ICCYCLECOUNTENTRY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ICCYCLECOUNTENTRY records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ICCYCLECOUNTENTRY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ICCYCLECOUNTENTRY.

Valid fields (from Docs samples):
- CYCLECOUNTKEY
- ITEMID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ICCYCLECOUNTENTRY.

Valid fields (from Docs samples):
- ADJUSTMENTREASON
- COUNTEDBYID
- QUANTITYCOUNTED
- QUANTITYDAMAGED
- RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ICCYCLECOUNTENTRY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class IcrowService(ObjectService):
    """Service for ICROW."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ICROW")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ICROW records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ICROW records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ICROW.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ICROW.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ICROW.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class IctransferService(ObjectService):
    """Service for ICTRANSFER."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ICTRANSFER")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ICTRANSFER records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ICTRANSFER records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ICTRANSFER.

Valid fields (from Docs samples):
- DESCRIPTION
- ICTRANSFERITEMS.ICTRANSFERITEM.IN_OUT
- ICTRANSFERITEMS.ICTRANSFERITEM.ITEMID
- ICTRANSFERITEMS.ICTRANSFERITEM.LOCATIONID
- ICTRANSFERITEMS.ICTRANSFERITEM.QUANTITY
- ICTRANSFERITEMS.ICTRANSFERITEM.UNIT
- ICTRANSFERITEMS.ICTRANSFERITEM.WAREHOUSEID
- TRANSACTIONDATE
- TRANSFERTYPE"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ICTRANSFER.

Valid fields (from Docs samples):
- ACTION
- DESCRIPTION
- ICTRANSFERITEMS.ICTRANSFERITEM.IN_OUT
- ICTRANSFERITEMS.ICTRANSFERITEM.ITEMID
- ICTRANSFERITEMS.ICTRANSFERITEM.LOCATIONID
- ICTRANSFERITEMS.ICTRANSFERITEM.QUANTITY
- ICTRANSFERITEMS.ICTRANSFERITEM.UNIT
- ICTRANSFERITEMS.ICTRANSFERITEM.WAREHOUSEID
- RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ICTRANSFER.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class InterentitysetupService(ObjectService):
    """Service for INTERENTITYSETUP."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "INTERENTITYSETUP")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read INTERENTITYSETUP records via readByQuery.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read INTERENTITYSETUP records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create INTERENTITYSETUP.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update INTERENTITYSETUP.

Valid fields (from Docs samples):
- ENTITYACCTDEFAULTS.ENTITYACCTDEFAULT.ENTITYID
- ENTITYACCTDEFAULTS.ENTITYACCTDEFAULT.IEPAYABLEACCTNO
- ENTITYACCTDEFAULTS.ENTITYACCTDEFAULT.IERECEIVABLEACCTNO
- ENTITYACCTDEFAULTS.ENTITYACCTDEFAULT.RECORDNO
- RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete INTERENTITYSETUP.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class InvdocumentService(ObjectService):
    """Service for INVDOCUMENT."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "INVDOCUMENT")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read INVDOCUMENT records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read INVDOCUMENT records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create INVDOCUMENT.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update INVDOCUMENT.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete INVDOCUMENT.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class InvdocumententryService(ObjectService):
    """Service for INVDOCUMENTENTRY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "INVDOCUMENTENTRY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read INVDOCUMENTENTRY records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read INVDOCUMENTENTRY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create INVDOCUMENTENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update INVDOCUMENTENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete INVDOCUMENTENTRY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class InvdocumentparamsService(ObjectService):
    """Service for INVDOCUMENTPARAMS."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "INVDOCUMENTPARAMS")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read INVDOCUMENTPARAMS records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read INVDOCUMENTPARAMS records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create INVDOCUMENTPARAMS.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update INVDOCUMENTPARAMS.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete INVDOCUMENTPARAMS.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class InvdocumentsubtotalsService(ObjectService):
    """Service for INVDOCUMENTSUBTOTALS."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "INVDOCUMENTSUBTOTALS")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read INVDOCUMENTSUBTOTALS records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read INVDOCUMENTSUBTOTALS records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create INVDOCUMENTSUBTOTALS.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update INVDOCUMENTSUBTOTALS.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete INVDOCUMENTSUBTOTALS.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class InventorytotaldetailService(ObjectService):
    """Service for INVENTORYTOTALDETAIL."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "INVENTORYTOTALDETAIL")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read INVENTORYTOTALDETAIL records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read INVENTORYTOTALDETAIL records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create INVENTORYTOTALDETAIL.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update INVENTORYTOTALDETAIL.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete INVENTORYTOTALDETAIL.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class InventorywqdetailService(ObjectService):
    """Service for INVENTORYWQDETAIL."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "INVENTORYWQDETAIL")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read INVENTORYWQDETAIL records via readByQuery.

Fields (from Docs samples):
- DOCID
- HOLDPROGRESS
- ICWQORDERID
- RECORDNO"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read INVENTORYWQDETAIL records.

Fields (from Docs samples):
- DOCID
- HOLDPROGRESS
- ICWQORDERID
- RECORDNO
- STATUS"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create INVENTORYWQDETAIL.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update INVENTORYWQDETAIL.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete INVENTORYWQDETAIL.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class InventorywqorderService(ObjectService):
    """Service for INVENTORYWQORDER."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "INVENTORYWQORDER")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read INVENTORYWQORDER records via readByQuery.

Fields (from Docs samples):
- CUSTOMERID
- ICWQORDERID
- PCTFULFILLABLE
- STATUS"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read INVENTORYWQORDER records.

Fields (from Docs samples):
- CUSTOMERID
- DOCID
- HOLDPROGRESS
- PCTFULFILLABLE
- STATUS"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create INVENTORYWQORDER.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update INVENTORYWQORDER.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete INVENTORYWQORDER.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class InvpricelistService(ObjectService):
    """Service for INVPRICELIST."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "INVPRICELIST")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read INVPRICELIST records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read INVPRICELIST records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create INVPRICELIST.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update INVPRICELIST.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete INVPRICELIST.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ItemService(ObjectService):
    """Service for ITEM."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ITEM")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ITEM records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ITEM records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ITEM.

Valid fields (from Docs samples):
- ITEMID
- ITEMTYPE
- NAME"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ITEM.

Valid fields (from Docs samples):
- NAME
- RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ITEM.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ItemcrossrefService(ObjectService):
    """Service for ITEMCROSSREF."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ITEMCROSSREF")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ITEMCROSSREF records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ITEMCROSSREF records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ITEMCROSSREF.

Valid fields (from Docs samples):
- ITEMALIASDESC
- ITEMALIASID
- ITEMID
- REFTYPE
- VENDORID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ITEMCROSSREF.

Valid fields (from Docs samples):
- ITEMALIASDESC
- RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ITEMCROSSREF.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ItemglgroupService(ObjectService):
    """Service for ITEMGLGROUP."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ITEMGLGROUP")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ITEMGLGROUP records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ITEMGLGROUP records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ITEMGLGROUP.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ITEMGLGROUP.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ITEMGLGROUP.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ItemgroupService(ObjectService):
    """Service for ITEMGROUP."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ITEMGROUP")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ITEMGROUP records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ITEMGROUP records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ITEMGROUP.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ITEMGROUP.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ITEMGROUP.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ItemtaxgroupService(ObjectService):
    """Service for ITEMTAXGROUP."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ITEMTAXGROUP")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ITEMTAXGROUP records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ITEMTAXGROUP records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ITEMTAXGROUP.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ITEMTAXGROUP.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ITEMTAXGROUP.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ItemwarehouseinfoService(ObjectService):
    """Service for ITEMWAREHOUSEINFO."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ITEMWAREHOUSEINFO")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ITEMWAREHOUSEINFO records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ITEMWAREHOUSEINFO records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ITEMWAREHOUSEINFO.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ITEMWAREHOUSEINFO.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ITEMWAREHOUSEINFO.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class JobqueuerecordService(ObjectService):
    """Service for JOBQUEUERECORD."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "JOBQUEUERECORD")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read JOBQUEUERECORD records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read JOBQUEUERECORD records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create JOBQUEUERECORD.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update JOBQUEUERECORD.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete JOBQUEUERECORD.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class LaborclassService(ObjectService):
    """Service for LABORCLASS."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "LABORCLASS")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read LABORCLASS records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read LABORCLASS records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create LABORCLASS.

Valid fields (from Docs samples):
- DESCRIPTION
- LABORCLASSID
- NAME"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update LABORCLASS.

Valid fields (from Docs samples):
- LABORCLASSID
- NAME"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete LABORCLASS.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class LaborshiftService(ObjectService):
    """Service for LABORSHIFT."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "LABORSHIFT")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read LABORSHIFT records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read LABORSHIFT records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create LABORSHIFT.

Valid fields (from Docs samples):
- DESCRIPTION
- LABORSHIFTID
- NAME"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update LABORSHIFT.

Valid fields (from Docs samples):
- DESCRIPTION
- LABORSHIFTID"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete LABORSHIFT.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class LaborunionService(ObjectService):
    """Service for LABORUNION."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "LABORUNION")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read LABORUNION records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read LABORUNION records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create LABORUNION.

Valid fields (from Docs samples):
- DESCRIPTION
- LABORUNIONID
- NAME"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update LABORUNION.

Valid fields (from Docs samples):
- DESCRIPTION
- LABORUNIONID"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete LABORUNION.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class LocationService(ObjectService):
    """Service for LOCATION."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "LOCATION")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read LOCATION records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read LOCATION records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create LOCATION.

Valid fields (from Docs samples):
- CONTACTINFO.CONTACTNAME
- CUSTTITLE
- ENDDATE
- LOCATIONID
- NAME
- PARENTID
- SHIPTO.CONTACTNAME
- STARTDATE
- STATUS
- SUPERVISORID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update LOCATION.

Valid fields (from Docs samples):
- CONTACTINFO.CONTACTNAME
- CUSTTITLE
- ENDDATE
- NAME
- PARENTID
- RECORDNO
- SHIPTO.CONTACTNAME
- STARTDATE
- STATUS
- SUPERVISORID"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete LOCATION.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class LocationentityService(ObjectService):
    """Service for LOCATIONENTITY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "LOCATIONENTITY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read LOCATIONENTITY records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read LOCATIONENTITY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create LOCATIONENTITY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update LOCATIONENTITY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete LOCATIONENTITY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class LocationgroupService(ObjectService):
    """Service for LOCATIONGROUP."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "LOCATIONGROUP")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read LOCATIONGROUP records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read LOCATIONGROUP records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create LOCATIONGROUP.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update LOCATIONGROUP.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete LOCATIONGROUP.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class MemberusergroupService(ObjectService):
    """Service for MEMBERUSERGROUP."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "MEMBERUSERGROUP")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read MEMBERUSERGROUP records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read MEMBERUSERGROUP records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create MEMBERUSERGROUP.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update MEMBERUSERGROUP.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete MEMBERUSERGROUP.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ObspctcompletedService(ObjectService):
    """Service for OBSPCTCOMPLETED."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "OBSPCTCOMPLETED")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read OBSPCTCOMPLETED records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read OBSPCTCOMPLETED records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create OBSPCTCOMPLETED.

Valid fields (from Docs samples):
- ASOFDATE
- NOTE
- PERCENT
- PROJECTKEY
- TASKKEY
- TYPE"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update OBSPCTCOMPLETED.

Valid fields (from Docs samples):
- PERCENT
- RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete OBSPCTCOMPLETED.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class OtherreceiptsService(ObjectService):
    """Service for OTHERRECEIPTS."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "OTHERRECEIPTS")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read OTHERRECEIPTS records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read OTHERRECEIPTS records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create OTHERRECEIPTS.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update OTHERRECEIPTS.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete OTHERRECEIPTS.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class OtherreceiptsentryService(ObjectService):
    """Service for OTHERRECEIPTSENTRY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "OTHERRECEIPTSENTRY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read OTHERRECEIPTSENTRY records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read OTHERRECEIPTSENTRY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create OTHERRECEIPTSENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update OTHERRECEIPTSENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete OTHERRECEIPTSENTRY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class PayrollreportcheckService(ObjectService):
    """Service for PAYROLLREPORTCHECK."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "PAYROLLREPORTCHECK")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read PAYROLLREPORTCHECK records via readByQuery.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read PAYROLLREPORTCHECK records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create PAYROLLREPORTCHECK.

Valid fields (from Docs samples):
- CHECKID
- CHECKSTATUS
- CHECKTYPE
- EMPLOYEEID
- EXTERNALENTITYID
- LEGALENTITYID
- PAYPERIODNUMBER
- PAYROLLYEAR
- REVISIONNUMBER"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update PAYROLLREPORTCHECK.

Valid fields (from Docs samples):
- CHECKSTATUS
- RECORDNO
- REVISIONNUMBER"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete PAYROLLREPORTCHECK.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class PayrollreportemployeeService(ObjectService):
    """Service for PAYROLLREPORTEMPLOYEE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "PAYROLLREPORTEMPLOYEE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read PAYROLLREPORTEMPLOYEE records via readByQuery.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read PAYROLLREPORTEMPLOYEE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create PAYROLLREPORTEMPLOYEE.

Valid fields (from Docs samples):
- EFFECTIVEDATE
- EMPLOYEEID
- PAYGROUPID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update PAYROLLREPORTEMPLOYEE.

Valid fields (from Docs samples):
- ACCEPTSELECTRONICW2
- PAYGROUPID
- RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete PAYROLLREPORTEMPLOYEE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class PayrollreportgrosspayService(ObjectService):
    """Service for PAYROLLREPORTGROSSPAY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "PAYROLLREPORTGROSSPAY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read PAYROLLREPORTGROSSPAY records via readByQuery.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read PAYROLLREPORTGROSSPAY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create PAYROLLREPORTGROSSPAY.

Valid fields (from Docs samples):
- CHECKID
- EMPLOYEEID
- GROSSPAY
- GROSSPAYID
- ISPREMIUM
- TIMECARDID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update PAYROLLREPORTGROSSPAY.

Valid fields (from Docs samples):
- HOURS
- RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete PAYROLLREPORTGROSSPAY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class PayrollreportpaymodifierService(ObjectService):
    """Service for PAYROLLREPORTPAYMODIFIER."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "PAYROLLREPORTPAYMODIFIER")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read PAYROLLREPORTPAYMODIFIER records via readByQuery.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read PAYROLLREPORTPAYMODIFIER records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create PAYROLLREPORTPAYMODIFIER.

Valid fields (from Docs samples):
- CHECKID
- EMPLOYEEID
- PAYMODIFIERCATEGORY
- PAYMODIFIERID
- PAYMODIFIERTYPE
- PRETAXCATCHUPCONTRIBUTIONAMT
- PRETAXCONTRIBUTIONAMT
- TIMECARDID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update PAYROLLREPORTPAYMODIFIER.

Valid fields (from Docs samples):
- PRETAXCATCHUPCONTRIBUTIONAMT
- PRETAXCONTRIBUTIONAMT"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete PAYROLLREPORTPAYMODIFIER.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class PayrollreportptoaccrualscheduleService(ObjectService):
    """Service for PAYROLLREPORTPTOACCRUALSCHEDULE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "PAYROLLREPORTPTOACCRUALSCHEDULE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read PAYROLLREPORTPTOACCRUALSCHEDULE records via readByQuery.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read PAYROLLREPORTPTOACCRUALSCHEDULE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create PAYROLLREPORTPTOACCRUALSCHEDULE.

Valid fields (from Docs samples):
- EFFECTIVEDATE
- PAYROLLREPORTPTOACCRUALSCHEDULELINES.PAYROLLREPORTPTOACCRUALSCHEDULELINE.MINIMUMYEARSOFSERVICE
- PAYROLLREPORTPTOACCRUALSCHEDULELINES.PAYROLLREPORTPTOACCRUALSCHEDULELINE.PAYROLLREPORTPTOACCRUALSCHEDULERATES.PAYROLLREPORTPTOACCRUALSCHEDULERATE.WORKEDHOURSID
- PTOACCRUALSCHEDULEID
- PTOTYPEID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update PAYROLLREPORTPTOACCRUALSCHEDULE.

Valid fields (from Docs samples):
- PTOTYPEID
- RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete PAYROLLREPORTPTOACCRUALSCHEDULE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class PayrollreportptoactivityService(ObjectService):
    """Service for PAYROLLREPORTPTOACTIVITY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "PAYROLLREPORTPTOACTIVITY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read PAYROLLREPORTPTOACTIVITY records via readByQuery.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read PAYROLLREPORTPTOACTIVITY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create PAYROLLREPORTPTOACTIVITY.

Valid fields (from Docs samples):
- ACCRUALSCHEDULEID
- CHECKID
- DEDUCTIONTAKEN
- EMPLOYEEID
- HOURS
- PTOACTIVITYID
- SOURCE
- TIMECARDID
- WORKEDHOURSID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update PAYROLLREPORTPTOACTIVITY.

Valid fields (from Docs samples):
- HOURS
- RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete PAYROLLREPORTPTOACTIVITY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class PayrollreporttaxService(ObjectService):
    """Service for PAYROLLREPORTTAX."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "PAYROLLREPORTTAX")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read PAYROLLREPORTTAX records via readByQuery.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read PAYROLLREPORTTAX records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create PAYROLLREPORTTAX.

Valid fields (from Docs samples):
- CHECKID
- EMPLOYEEID
- EMPLOYEETAXAMOUNT
- EMPLOYERTAXAMOUNT
- TAXCATEGORYID
- TAXID
- TIMECARDID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update PAYROLLREPORTTAX.

Valid fields (from Docs samples):
- EMPLOYEETAXAMOUNT
- EMPLOYERTAXAMOUNT
- RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete PAYROLLREPORTTAX.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class PayrollreporttaxsetupService(ObjectService):
    """Service for PAYROLLREPORTTAXSETUP."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "PAYROLLREPORTTAXSETUP")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read PAYROLLREPORTTAXSETUP records via readByQuery.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read PAYROLLREPORTTAXSETUP records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create PAYROLLREPORTTAXSETUP.

Valid fields (from Docs samples):
- REPORTAS
- REPORTINGLEVEL
- STATE
- TAXCATEGORYID
- TAXID
- TAXTYPE"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update PAYROLLREPORTTAXSETUP.

Valid fields (from Docs samples):
- RECORDNO
- TAXCATEGORYID"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete PAYROLLREPORTTAXSETUP.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class PayrollreporttimecardService(ObjectService):
    """Service for PAYROLLREPORTTIMECARD."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "PAYROLLREPORTTIMECARD")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read PAYROLLREPORTTIMECARD records via readByQuery.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read PAYROLLREPORTTIMECARD records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create PAYROLLREPORTTIMECARD.

Valid fields (from Docs samples):
- CHECKID
- COSTTYPEID
- EMPLOYEEID
- HOMEUNIONID
- LOCATIONID
- PROJECTID
- TASKID
- TIMECARDID
- TRADEID
- TRADELEVELID
- WORKDATE
- WORKUNIONID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update PAYROLLREPORTTIMECARD.

Valid fields (from Docs samples):
- RECORDNO
- WORKDATE"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete PAYROLLREPORTTIMECARD.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class PayrollreporttradeService(ObjectService):
    """Service for PAYROLLREPORTTRADE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "PAYROLLREPORTTRADE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read PAYROLLREPORTTRADE records via readByQuery.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read PAYROLLREPORTTRADE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create PAYROLLREPORTTRADE.

Valid fields (from Docs samples):
- PAYROLLREPORTTRADELEVEL.CLASSLEVEL
- PAYROLLREPORTTRADELEVEL.CLASSPERSCENT
- PAYROLLREPORTTRADELEVEL.TRADEKEY
- PAYROLLREPORTTRADELEVEL.TRADELEVELID
- REVISIONNUMBER
- TRADEID
- WORKCLASSIFICATION
- WORKCLASSIFICATIONCODE"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update PAYROLLREPORTTRADE.

Valid fields (from Docs samples):
- RECORDNO
- TRADEID"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete PAYROLLREPORTTRADE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class PjestimateService(ObjectService):
    """Service for PJESTIMATE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "PJESTIMATE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read PJESTIMATE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read PJESTIMATE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create PJESTIMATE.

Valid fields (from Docs samples):
- ENTRIES.PJESTIMATEENTRY.AMOUNT
- ENTRIES.PJESTIMATEENTRY.MEMO
- ENTRIES.PJESTIMATEENTRY.WFTYPE
- PJESTIMATEID
- PROJECTID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update PJESTIMATE.

Valid fields (from Docs samples):
- DESCRIPTION
- RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete PJESTIMATE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class PjestimateentryService(ObjectService):
    """Service for PJESTIMATEENTRY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "PJESTIMATEENTRY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read PJESTIMATEENTRY records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read PJESTIMATEENTRY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create PJESTIMATEENTRY.

Valid fields (from Docs samples):
- EUOM
- PJESTIMATEID
- QTY
- UNITCOST
- WFTYPE"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update PJESTIMATEENTRY.

Valid fields (from Docs samples):
- AMOUNT
- RECORDNO
- WFTYPE"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete PJESTIMATEENTRY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class PjestimatetypeService(ObjectService):
    """Service for PJESTIMATETYPE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "PJESTIMATETYPE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read PJESTIMATETYPE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read PJESTIMATETYPE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create PJESTIMATETYPE.

Valid fields (from Docs samples):
- NAME
- SELECTEDWFTYPES"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update PJESTIMATETYPE.

Valid fields (from Docs samples):
- NAME
- SELECTEDWFTYPES"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete PJESTIMATETYPE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class PodocumentService(ObjectService):
    """Service for PODOCUMENT."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "PODOCUMENT")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read PODOCUMENT records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read PODOCUMENT records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create PODOCUMENT.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update PODOCUMENT.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete PODOCUMENT.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class PodocumententryService(ObjectService):
    """Service for PODOCUMENTENTRY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "PODOCUMENTENTRY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read PODOCUMENTENTRY records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read PODOCUMENTENTRY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create PODOCUMENTENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update PODOCUMENTENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete PODOCUMENTENTRY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class PodocumentparamsService(ObjectService):
    """Service for PODOCUMENTPARAMS."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "PODOCUMENTPARAMS")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read PODOCUMENTPARAMS records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read PODOCUMENTPARAMS records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create PODOCUMENTPARAMS.

Valid fields (from Docs samples):
- ALLOWEDITBILLTO
- ALLOWEDITDELIVERTO
- ALLOWEDITSHIPTO
- AR_ACCOUNTS.AR_ACCOUNT.DEBIT_CREDIT
- AR_ACCOUNTS.AR_ACCOUNT.GLACCOUNT
- AR_ACCOUNTS.AR_ACCOUNT.ISOFFSET
- AR_ACCOUNTS.AR_ACCOUNT.ITEM_GLGROUP
- CATEGORY
- CONTACTTITLE1
- CONTACTTITLE2
- CONTACTTITLE3
- CONVTYPE
- CREATETYPE
- CREDITLIMITCHECK
- DELTYPE
- DESCRIPTION
- DOCCLASS
- DOCID
- EDITTYPE
- ENABLEOVERRIDETAX
- INHERIT_SOURCE_DOCNO
- LINELEVELSIMPLETAX
- OVERRIDE_PRICE
- POSTTOGL
- PRESERVE_SEQNUM
- RECALLS.RECALL.RECDOCPAR
- SEQUENCE
- SHOWEXPANDEDTOTALS
- SHOWTITLE1
- SHOWTITLE2
- SHOWTITLE3
- SHOW_TOTALS
- TD_CREATION_RULE
- UPDATES_GL"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update PODOCUMENTPARAMS.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete PODOCUMENTPARAMS.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class PodocumentsubtotalsService(ObjectService):
    """Service for PODOCUMENTSUBTOTALS."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "PODOCUMENTSUBTOTALS")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read PODOCUMENTSUBTOTALS records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read PODOCUMENTSUBTOTALS records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create PODOCUMENTSUBTOTALS.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update PODOCUMENTSUBTOTALS.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete PODOCUMENTSUBTOTALS.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class PopricelistService(ObjectService):
    """Service for POPRICELIST."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "POPRICELIST")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read POPRICELIST records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read POPRICELIST records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create POPRICELIST.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update POPRICELIST.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete POPRICELIST.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class PositionskillService(ObjectService):
    """Service for POSITIONSKILL."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "POSITIONSKILL")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read POSITIONSKILL records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read POSITIONSKILL records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create POSITIONSKILL.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update POSITIONSKILL.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete POSITIONSKILL.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class PosubtotaltemplateService(ObjectService):
    """Service for POSUBTOTALTEMPLATE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "POSUBTOTALTEMPLATE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read POSUBTOTALTEMPLATE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read POSUBTOTALTEMPLATE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create POSUBTOTALTEMPLATE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update POSUBTOTALTEMPLATE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete POSUBTOTALTEMPLATE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ProductlineService(ObjectService):
    """Service for PRODUCTLINE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "PRODUCTLINE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read PRODUCTLINE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read PRODUCTLINE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create PRODUCTLINE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update PRODUCTLINE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete PRODUCTLINE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ProjectService(ObjectService):
    """Service for PROJECT."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "PROJECT")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read PROJECT records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read PROJECT records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create PROJECT.

Valid fields (from Docs samples):
- NAME
- PROJECTCATEGORY"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update PROJECT.

Valid fields (from Docs samples):
- NAME
- PROJECTID"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete PROJECT.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ProjectchangeorderService(ObjectService):
    """Service for PROJECTCHANGEORDER."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "PROJECTCHANGEORDER")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read PROJECTCHANGEORDER records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read PROJECTCHANGEORDER records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create PROJECTCHANGEORDER.

Valid fields (from Docs samples):
- CHANGEREQUESTSTATUSNAME
- ITEMID
- PROJECTCHANGEORDERDATE
- PROJECTCHANGEORDERID
- PROJECTID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update PROJECTCHANGEORDER.

Valid fields (from Docs samples):
- CHANGEREQUESTSTATUSNAME
- PROJECTCHANGEORDERID"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete PROJECTCHANGEORDER.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ProjectcontractService(ObjectService):
    """Service for PROJECTCONTRACT."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "PROJECTCONTRACT")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read PROJECTCONTRACT records via readByQuery.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read PROJECTCONTRACT records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create PROJECTCONTRACT.

Valid fields (from Docs samples):
- CONTRACTDATE
- CUSTOMERID
- NAME
- PROJECTCONTRACTID
- PROJECTID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update PROJECTCONTRACT.

Valid fields (from Docs samples):
- RECORDNO
- STATUS"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete PROJECTCONTRACT.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ProjectcontractlineService(ObjectService):
    """Service for PROJECTCONTRACTLINE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "PROJECTCONTRACTLINE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read PROJECTCONTRACTLINE records via readByQuery.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read PROJECTCONTRACTLINE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create PROJECTCONTRACTLINE.

Valid fields (from Docs samples):
- ACCOUNTNO
- BILLINGTYPE
- CONTRACTLINEDATE
- ITEMID
- MAXIMUMBILLING
- NAME
- PROJECTCONTRACTID
- PROJECTCONTRACTLINEID
- PROJECTID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update PROJECTCONTRACTLINE.

Valid fields (from Docs samples):
- RECORDNO
- STATUS"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete PROJECTCONTRACTLINE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ProjectcontractlineentryService(ObjectService):
    """Service for PROJECTCONTRACTLINEENTRY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "PROJECTCONTRACTLINEENTRY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read PROJECTCONTRACTLINEENTRY records via readByQuery.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read PROJECTCONTRACTLINEENTRY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create PROJECTCONTRACTLINEENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update PROJECTCONTRACTLINEENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete PROJECTCONTRACTLINEENTRY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ProjectcontracttypeService(ObjectService):
    """Service for PROJECTCONTRACTTYPE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "PROJECTCONTRACTTYPE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read PROJECTCONTRACTTYPE records via readByQuery.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read PROJECTCONTRACTTYPE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create PROJECTCONTRACTTYPE.

Valid fields (from Docs samples):
- PROJECTCONTRACTTYPEID
- PROJECTCONTRACTTYPENAME"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update PROJECTCONTRACTTYPE.

Valid fields (from Docs samples):
- PROJECTCONTRACTTYPE
- STATUS"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete PROJECTCONTRACTTYPE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ProjectgroupService(ObjectService):
    """Service for PROJECTGROUP."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "PROJECTGROUP")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read PROJECTGROUP records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read PROJECTGROUP records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create PROJECTGROUP.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update PROJECTGROUP.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete PROJECTGROUP.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ProjectresourcesService(ObjectService):
    """Service for PROJECTRESOURCES."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "PROJECTRESOURCES")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read PROJECTRESOURCES records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read PROJECTRESOURCES records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create PROJECTRESOURCES.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update PROJECTRESOURCES.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete PROJECTRESOURCES.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ProjectstatusService(ObjectService):
    """Service for PROJECTSTATUS."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "PROJECTSTATUS")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read PROJECTSTATUS records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read PROJECTSTATUS records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create PROJECTSTATUS.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update PROJECTSTATUS.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete PROJECTSTATUS.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ProjecttypeService(ObjectService):
    """Service for PROJECTTYPE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "PROJECTTYPE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read PROJECTTYPE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read PROJECTTYPE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create PROJECTTYPE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update PROJECTTYPE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete PROJECTTYPE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ProviderbankaccountService(ObjectService):
    """Service for PROVIDERBANKACCOUNT."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "PROVIDERBANKACCOUNT")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read PROVIDERBANKACCOUNT records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read PROVIDERBANKACCOUNT records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create PROVIDERBANKACCOUNT.

Valid fields (from Docs samples):
- PROVIDERID
- VENDORID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update PROVIDERBANKACCOUNT.

Valid fields (from Docs samples):
- RECORDNO
- STATUS"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete PROVIDERBANKACCOUNT.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ProviderpaymentmethodService(ObjectService):
    """Service for PROVIDERPAYMENTMETHOD."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "PROVIDERPAYMENTMETHOD")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read PROVIDERPAYMENTMETHOD records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read PROVIDERPAYMENTMETHOD records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create PROVIDERPAYMENTMETHOD.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update PROVIDERPAYMENTMETHOD.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete PROVIDERPAYMENTMETHOD.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ProvidervendorService(ObjectService):
    """Service for PROVIDERVENDOR."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "PROVIDERVENDOR")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read PROVIDERVENDOR records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read PROVIDERVENDOR records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create PROVIDERVENDOR.

Valid fields (from Docs samples):
- PROVIDERID
- STATUS
- VENDORID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update PROVIDERVENDOR.

Valid fields (from Docs samples):
- RECORDNO
- STATUS"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete PROVIDERVENDOR.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class PtapplicationService(ObjectService):
    """Service for PTAPPLICATION."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "PTAPPLICATION")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read PTAPPLICATION records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read PTAPPLICATION records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create PTAPPLICATION.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update PTAPPLICATION.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete PTAPPLICATION.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class RatetableService(ObjectService):
    """Service for RATETABLE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "RATETABLE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read RATETABLE records via readByQuery.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read RATETABLE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create RATETABLE.

Valid fields (from Docs samples):
- RATETABLEID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update RATETABLE.

Valid fields (from Docs samples):
- RATETABLECCENTRIES.RATETABLECCENTRY.ACCUMULATIONTYPENAME
- RATETABLECCENTRIES.RATETABLECCENTRY.DESCRIPTION
- RATETABLECCENTRIES.RATETABLECCENTRY.EMPLOYEEID
- RATETABLECCENTRIES.RATETABLECCENTRY.ITEMID
- RATETABLECCENTRIES.RATETABLECCENTRY.MARKUPPCT
- RATETABLECCENTRIES.RATETABLECCENTRY.STANDARDCOSTTYPEID
- RATETABLECCENTRIES.RATETABLECCENTRY.STANDARDTASKID
- RATETABLECCENTRIES.RATETABLECCENTRY.STARTDATE
- RATETABLEID"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete RATETABLE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class RatetableapentryService(ObjectService):
    """Service for RATETABLEAPENTRY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "RATETABLEAPENTRY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read RATETABLEAPENTRY records via readByQuery.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read RATETABLEAPENTRY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create RATETABLEAPENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update RATETABLEAPENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete RATETABLEAPENTRY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class RatetablepoentryService(ObjectService):
    """Service for RATETABLEPOENTRY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "RATETABLEPOENTRY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read RATETABLEPOENTRY records via readByQuery.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read RATETABLEPOENTRY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create RATETABLEPOENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update RATETABLEPOENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete RATETABLEPOENTRY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class RatetabletsentryService(ObjectService):
    """Service for RATETABLETSENTRY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "RATETABLETSENTRY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read RATETABLETSENTRY records via readByQuery.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read RATETABLETSENTRY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create RATETABLETSENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update RATETABLETSENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete RATETABLETSENTRY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class RecurglacctallocationService(ObjectService):
    """Service for RECURGLACCTALLOCATION."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "RECURGLACCTALLOCATION")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read RECURGLACCTALLOCATION records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read RECURGLACCTALLOCATION records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create RECURGLACCTALLOCATION.

Valid fields (from Docs samples):
- EMAIL
- ENDINGON
- GLACCTALLOCATION
- ISPERIODEND
- PLANNAME
- REPEATBY
- REPEATINTERVAL
- STARTDATE"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update RECURGLACCTALLOCATION.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete RECURGLACCTALLOCATION.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ReportingperiodService(ObjectService):
    """Service for REPORTINGPERIOD."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "REPORTINGPERIOD")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read REPORTINGPERIOD records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read REPORTINGPERIOD records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create REPORTINGPERIOD.

Valid fields (from Docs samples):
- BUDGETING
- END_DATE
- HEADER1
- HEADER2
- NAME
- START_DATE
- STATUS"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update REPORTINGPERIOD.

Valid fields (from Docs samples):
- BUDGETING
- END_DATE
- HEADER1
- HEADER2
- RECORDNO
- START_DATE
- STATUS"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete REPORTINGPERIOD.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class RevrecscheduleService(ObjectService):
    """Service for REVRECSCHEDULE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "REVRECSCHEDULE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read REVRECSCHEDULE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read REVRECSCHEDULE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create REVRECSCHEDULE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update REVRECSCHEDULE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete REVRECSCHEDULE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class RevrecscheduleentryService(ObjectService):
    """Service for REVRECSCHEDULEENTRY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "REVRECSCHEDULEENTRY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read REVRECSCHEDULEENTRY records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read REVRECSCHEDULEENTRY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create REVRECSCHEDULEENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update REVRECSCHEDULEENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete REVRECSCHEDULEENTRY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class RoleassignmentService(ObjectService):
    """Service for ROLEASSIGNMENT."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ROLEASSIGNMENT")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ROLEASSIGNMENT records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ROLEASSIGNMENT records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ROLEASSIGNMENT.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ROLEASSIGNMENT.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ROLEASSIGNMENT.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class RolegroupsService(ObjectService):
    """Service for ROLEGROUPS."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ROLEGROUPS")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ROLEGROUPS records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ROLEGROUPS records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ROLEGROUPS.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ROLEGROUPS.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ROLEGROUPS.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class RolepolicyassignmentService(ObjectService):
    """Service for ROLEPOLICYASSIGNMENT."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ROLEPOLICYASSIGNMENT")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ROLEPOLICYASSIGNMENT records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ROLEPOLICYASSIGNMENT records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ROLEPOLICYASSIGNMENT.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ROLEPOLICYASSIGNMENT.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ROLEPOLICYASSIGNMENT.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class RolesService(ObjectService):
    """Service for ROLES."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ROLES")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ROLES records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ROLES records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ROLES.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ROLES.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ROLES.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class RoleusersService(ObjectService):
    """Service for ROLEUSERS."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ROLEUSERS")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ROLEUSERS records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ROLEUSERS records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ROLEUSERS.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ROLEUSERS.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ROLEUSERS.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class SavingsaccountService(ObjectService):
    """Service for SAVINGSACCOUNT."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "SAVINGSACCOUNT")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read SAVINGSACCOUNT records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read SAVINGSACCOUNT records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create SAVINGSACCOUNT.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update SAVINGSACCOUNT.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete SAVINGSACCOUNT.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class SodocumentService(ObjectService):
    """Service for SODOCUMENT."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "SODOCUMENT")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read SODOCUMENT records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read SODOCUMENT records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create SODOCUMENT.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update SODOCUMENT.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete SODOCUMENT.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class SodocumententryService(ObjectService):
    """Service for SODOCUMENTENTRY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "SODOCUMENTENTRY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read SODOCUMENTENTRY records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read SODOCUMENTENTRY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create SODOCUMENTENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update SODOCUMENTENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete SODOCUMENTENTRY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class SodocumentparamsService(ObjectService):
    """Service for SODOCUMENTPARAMS."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "SODOCUMENTPARAMS")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read SODOCUMENTPARAMS records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read SODOCUMENTPARAMS records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create SODOCUMENTPARAMS.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update SODOCUMENTPARAMS.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete SODOCUMENTPARAMS.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class SodocumentsubtotalsService(ObjectService):
    """Service for SODOCUMENTSUBTOTALS."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "SODOCUMENTSUBTOTALS")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read SODOCUMENTSUBTOTALS records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read SODOCUMENTSUBTOTALS records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create SODOCUMENTSUBTOTALS.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update SODOCUMENTSUBTOTALS.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete SODOCUMENTSUBTOTALS.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class SopricelistService(ObjectService):
    """Service for SOPRICELIST."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "SOPRICELIST")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read SOPRICELIST records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read SOPRICELIST records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create SOPRICELIST.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update SOPRICELIST.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete SOPRICELIST.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class SorecurdocumentService(ObjectService):
    """Service for SORECURDOCUMENT."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "SORECURDOCUMENT")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read SORECURDOCUMENT records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read SORECURDOCUMENT records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create SORECURDOCUMENT.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update SORECURDOCUMENT.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete SORECURDOCUMENT.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class SosubtotaltemplateService(ObjectService):
    """Service for SOSUBTOTALTEMPLATE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "SOSUBTOTALTEMPLATE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read SOSUBTOTALTEMPLATE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read SOSUBTOTALTEMPLATE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create SOSUBTOTALTEMPLATE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update SOSUBTOTALTEMPLATE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete SOSUBTOTALTEMPLATE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class StandardcosttypeService(ObjectService):
    """Service for STANDARDCOSTTYPE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "STANDARDCOSTTYPE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read STANDARDCOSTTYPE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read STANDARDCOSTTYPE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create STANDARDCOSTTYPE.

Valid fields (from Docs samples):
- COSTUNITDESCRIPTION
- DESCRIPTION
- NAME
- STANDARDCOSTTYPEID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update STANDARDCOSTTYPE.

Valid fields (from Docs samples):
- DESCRIPTION
- STANDARDCOSTTYPEID"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete STANDARDCOSTTYPE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class StandardtaskService(ObjectService):
    """Service for STANDARDTASK."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "STANDARDTASK")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read STANDARDTASK records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read STANDARDTASK records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create STANDARDTASK.

Valid fields (from Docs samples):
- COSTUNITDESCRIPTION
- DESCRIPTION
- NAME
- STANDARDTASKID
- STANDARDTASKSTANDARDCOSTTYPES.STANDARDTASKSTANDARDCOSTTYPE.STANDARDCOSTTYPEID
- TASKNO
- TIMETYPENAME"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update STANDARDTASK.

Valid fields (from Docs samples):
- STANDARDTASKID
- TIMETYPENAME"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete STANDARDTASK.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class StataccountService(ObjectService):
    """Service for STATACCOUNT."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "STATACCOUNT")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read STATACCOUNT records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read STATACCOUNT records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create STATACCOUNT.

Valid fields (from Docs samples):
- ACCOUNTNO
- TITLE"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update STATACCOUNT.

Valid fields (from Docs samples):
- RECORDNO
- TITLE"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete STATACCOUNT.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class TaskService(ObjectService):
    """Service for TASK."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "TASK")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read TASK records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read TASK records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create TASK.

Valid fields (from Docs samples):
- NAME
- PROJECTID
- TASKID
- TASKSTATUS"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update TASK.

Valid fields (from Docs samples):
- PROJECTID
- RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete TASK.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class TaskresourcesService(ObjectService):
    """Service for TASKRESOURCES."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "TASKRESOURCES")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read TASKRESOURCES records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read TASKRESOURCES records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create TASKRESOURCES.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update TASKRESOURCES.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete TASKRESOURCES.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class TaxdetailService(ObjectService):
    """Service for TAXDETAIL."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "TAXDETAIL")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read TAXDETAIL records via readByQuery.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read TAXDETAIL records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create TAXDETAIL.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update TAXDETAIL.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete TAXDETAIL.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class TaxrecordService(ObjectService):
    """Service for TAXRECORD."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "TAXRECORD")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read TAXRECORD records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read TAXRECORD records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create TAXRECORD.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update TAXRECORD.

Valid fields (from Docs samples):
- MCA_NOTES
- RECORDNO"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete TAXRECORD.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class TaxsolutionService(ObjectService):
    """Service for TAXSOLUTION."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "TAXSOLUTION")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read TAXSOLUTION records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read TAXSOLUTION records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create TAXSOLUTION.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update TAXSOLUTION.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete TAXSOLUTION.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class TimesheetService(ObjectService):
    """Service for TIMESHEET."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "TIMESHEET")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read TIMESHEET records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read TIMESHEET records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create TIMESHEET.

Valid fields (from Docs samples):
- BEGINDATE
- DESCRIPTION
- EMPLOYEEID
- GLPOSTDATE
- STATE
- SUPDOCID
- TIMESHEETENTRIES.TIMESHEETENTRY.BILLABLE
- TIMESHEETENTRIES.TIMESHEETENTRY.CLASSID
- TIMESHEETENTRIES.TIMESHEETENTRY.CUSTOMERID
- TIMESHEETENTRIES.TIMESHEETENTRY.DEPARTMENTID
- TIMESHEETENTRIES.TIMESHEETENTRY.DESCRIPTION
- TIMESHEETENTRIES.TIMESHEETENTRY.EMPLOYEEID
- TIMESHEETENTRIES.TIMESHEETENTRY.ENTRYDATE
- TIMESHEETENTRIES.TIMESHEETENTRY.EXTBILLRATE
- TIMESHEETENTRIES.TIMESHEETENTRY.EXTCOSTRATE
- TIMESHEETENTRIES.TIMESHEETENTRY.ITEMID
- TIMESHEETENTRIES.TIMESHEETENTRY.LOCATIONID
- TIMESHEETENTRIES.TIMESHEETENTRY.NOTES
- TIMESHEETENTRIES.TIMESHEETENTRY.PROJECTID
- TIMESHEETENTRIES.TIMESHEETENTRY.QTY
- TIMESHEETENTRIES.TIMESHEETENTRY.TASKKEY
- TIMESHEETENTRIES.TIMESHEETENTRY.TIMETYPE
- TIMESHEETENTRIES.TIMESHEETENTRY.VENDORID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update TIMESHEET.

Valid fields (from Docs samples):
- BEGINDATE
- DESCRIPTION
- EMPLOYEEID
- GLPOSTDATE
- RECORDNO
- STATE
- SUPDOCID
- TIMESHEETENTRIES.TIMESHEETENTRY.BILLABLE
- TIMESHEETENTRIES.TIMESHEETENTRY.CLASSID
- TIMESHEETENTRIES.TIMESHEETENTRY.CUSTOMERID
- TIMESHEETENTRIES.TIMESHEETENTRY.DEPARTMENTID
- TIMESHEETENTRIES.TIMESHEETENTRY.DESCRIPTION
- TIMESHEETENTRIES.TIMESHEETENTRY.EMPLOYEEID
- TIMESHEETENTRIES.TIMESHEETENTRY.ENTRYDATE
- TIMESHEETENTRIES.TIMESHEETENTRY.EXTBILLRATE
- TIMESHEETENTRIES.TIMESHEETENTRY.EXTCOSTRATE
- TIMESHEETENTRIES.TIMESHEETENTRY.ITEMID
- TIMESHEETENTRIES.TIMESHEETENTRY.LOCATIONID
- TIMESHEETENTRIES.TIMESHEETENTRY.NOTES
- TIMESHEETENTRIES.TIMESHEETENTRY.PROJECTID
- TIMESHEETENTRIES.TIMESHEETENTRY.QTY
- TIMESHEETENTRIES.TIMESHEETENTRY.TASKKEY
- TIMESHEETENTRIES.TIMESHEETENTRY.TIMETYPE
- TIMESHEETENTRIES.TIMESHEETENTRY.VENDORID"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete TIMESHEET.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class TimesheetapprovalService(ObjectService):
    """Service for TIMESHEETAPPROVAL."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "TIMESHEETAPPROVAL")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read TIMESHEETAPPROVAL records via readByQuery.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read TIMESHEETAPPROVAL records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create TIMESHEETAPPROVAL.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update TIMESHEETAPPROVAL.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete TIMESHEETAPPROVAL.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class TimesheetentryService(ObjectService):
    """Service for TIMESHEETENTRY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "TIMESHEETENTRY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read TIMESHEETENTRY records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read TIMESHEETENTRY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create TIMESHEETENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update TIMESHEETENTRY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete TIMESHEETENTRY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class TimetypeService(ObjectService):
    """Service for TIMETYPE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "TIMETYPE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read TIMETYPE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read TIMETYPE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create TIMETYPE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update TIMETYPE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete TIMETYPE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class TransactionruleService(ObjectService):
    """Service for TRANSACTIONRULE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "TRANSACTIONRULE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read TRANSACTIONRULE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read TRANSACTIONRULE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create TRANSACTIONRULE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update TRANSACTIONRULE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete TRANSACTIONRULE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class TransactionruledetailService(ObjectService):
    """Service for TRANSACTIONRULEDETAIL."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "TRANSACTIONRULEDETAIL")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read TRANSACTIONRULEDETAIL records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read TRANSACTIONRULEDETAIL records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create TRANSACTIONRULEDETAIL.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update TRANSACTIONRULEDETAIL.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete TRANSACTIONRULEDETAIL.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class UomService(ObjectService):
    """Service for UOM."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "UOM")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read UOM records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read UOM records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create UOM.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update UOM.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete UOM.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class UomdetailService(ObjectService):
    """Service for UOMDETAIL."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "UOMDETAIL")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read UOMDETAIL records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read UOMDETAIL records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create UOMDETAIL.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update UOMDETAIL.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete UOMDETAIL.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class UsergroupService(ObjectService):
    """Service for USERGROUP."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "USERGROUP")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read USERGROUP records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read USERGROUP records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create USERGROUP.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update USERGROUP.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete USERGROUP.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class UserinfoService(ObjectService):
    """Service for USERINFO."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "USERINFO")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read USERINFO records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read USERINFO records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create USERINFO.

Valid fields (from Docs samples):
- ADMIN
- CONTACTINFO.EMAIL1
- CONTACTINFO.FIRSTNAME
- CONTACTINFO.LASTNAME
- DESCRIPTION
- LOGINID
- SSO_ENABLED
- SSO_FEDERATED_ID
- STATUS
- USERTYPE"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update USERINFO.

Valid fields (from Docs samples):
- RECORDNO
- USERDEPARTMENTS.DEPARTMENTID
- USERLOCATIONS.LOCATIONID"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete USERINFO.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class UserrestrictionService(ObjectService):
    """Service for USERRESTRICTION."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "USERRESTRICTION")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read USERRESTRICTION records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read USERRESTRICTION records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create USERRESTRICTION.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update USERRESTRICTION.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete USERRESTRICTION.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class UserrightsService(ObjectService):
    """Service for USERRIGHTS."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "USERRIGHTS")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read USERRIGHTS records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read USERRIGHTS records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create USERRIGHTS.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update USERRIGHTS.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete USERRIGHTS.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class UserrolesService(ObjectService):
    """Service for USERROLES."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "USERROLES")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read USERROLES records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read USERROLES records.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create USERROLES.

Valid fields (from Docs samples):
- ROLENAME
- USERID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update USERROLES.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete USERROLES.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class VendorService(ObjectService):
    """Service for VENDOR."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "VENDOR")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read VENDOR records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read VENDOR records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create VENDOR.

Valid fields (from Docs samples):
- ACHACCOUNTNUMBER
- ACHACCOUNTTYPE
- ACHBANKROUTINGNUMBER
- ACHENABLED
- ACHREMITTANCETYPE
- APACCOUNT
- BILLINGTYPE
- COMMENTS
- CONTACTINFO.CONTACTNAME
- CREDITLIMIT
- CURRENCY
- CUSTOMFIELD1
- DISPLAYACCTNOCHECK
- DISPLAYCONTACT.CELLPHONE
- DISPLAYCONTACT.COMPANYNAME
- DISPLAYCONTACT.EMAIL1
- DISPLAYCONTACT.EMAIL2
- DISPLAYCONTACT.FAX
- DISPLAYCONTACT.FIRSTNAME
- DISPLAYCONTACT.INITIAL
- DISPLAYCONTACT.LASTNAME
- DISPLAYCONTACT.MAILADDRESS.ADDRESS1
- DISPLAYCONTACT.MAILADDRESS.ADDRESS2
- DISPLAYCONTACT.MAILADDRESS.CITY
- DISPLAYCONTACT.MAILADDRESS.COUNTRY
- DISPLAYCONTACT.MAILADDRESS.STATE
- DISPLAYCONTACT.MAILADDRESS.ZIP
- DISPLAYCONTACT.PAGER
- DISPLAYCONTACT.PHONE1
- DISPLAYCONTACT.PHONE2
- DISPLAYCONTACT.PREFIX
- DISPLAYCONTACT.PRINTAS
- DISPLAYCONTACT.TAXABLE
- DISPLAYCONTACT.TAXGROUP
- DISPLAYCONTACT.TAXSCHEDULE
- DISPLAYCONTACT.TAXSOLUTIONID
- DISPLAYCONTACT.URL1
- DISPLAYCONTACT.URL2
- DISPLAYTERMDISCOUNT
- DONOTCUTCHECK
- FORM1099BOX
- FORM1099TYPE
- GLGROUP
- HIDEDISPLAYCONTACT
- MERGEPAYMENTREQ
- NAME
- NAME1099
- OBJECTRESTRICTION
- ONETIME
- ONHOLD
- PARENTID
- PAYMENTNOTIFY
- PAYMENTPRIORITY
- PAYMETHODKEY
- PAYTO.CONTACTNAME
- RESTRICTEDDEPARTMENTS
- RESTRICTEDLOCATIONS
- RETURNTO.CONTACTNAME
- STATUS
- SUPDOCID
- TAXID
- TERMNAME
- VCF_BILL_SITEID3
- VENDORACCOUNTNO
- VENDORID
- VENDTYPE"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update VENDOR.

Valid fields (from Docs samples):
- RECORDNO
- TERMNAME
- VCF_BILL_SITEID3"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete VENDOR.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class VendoremailtemplateService(ObjectService):
    """Service for VENDOREMAILTEMPLATE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "VENDOREMAILTEMPLATE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read VENDOREMAILTEMPLATE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read VENDOREMAILTEMPLATE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create VENDOREMAILTEMPLATE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update VENDOREMAILTEMPLATE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete VENDOREMAILTEMPLATE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class VendorgroupService(ObjectService):
    """Service for VENDORGROUP."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "VENDORGROUP")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read VENDORGROUP records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read VENDORGROUP records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create VENDORGROUP.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update VENDORGROUP.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete VENDORGROUP.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class VendorvisibilityService(ObjectService):
    """Service for VENDORVISIBILITY."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "VENDORVISIBILITY")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read VENDORVISIBILITY records via readByQuery.

Fields (from Docs samples):
- (no fields listed)"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read VENDORVISIBILITY records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create VENDORVISIBILITY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update VENDORVISIBILITY.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete VENDORVISIBILITY.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class VendtypeService(ObjectService):
    """Service for VENDTYPE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "VENDTYPE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read VENDTYPE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read VENDTYPE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create VENDTYPE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update VENDTYPE.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete VENDTYPE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class WarehouseService(ObjectService):
    """Service for WAREHOUSE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "WAREHOUSE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read WAREHOUSE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read WAREHOUSE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create WAREHOUSE.

Valid fields (from Docs samples):
- LOC.LOCATIONID
- NAME
- WAREHOUSEID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update WAREHOUSE.

Valid fields (from Docs samples):
- RECORDNO
- STATUS"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete WAREHOUSE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class WarehousegroupService(ObjectService):
    """Service for WAREHOUSEGROUP."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "WAREHOUSEGROUP")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read WAREHOUSEGROUP records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read WAREHOUSEGROUP records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create WAREHOUSEGROUP.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update WAREHOUSEGROUP.

Valid fields (from Docs samples):
- (no fields listed)"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete WAREHOUSEGROUP.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


class ZoneService(ObjectService):
    """Service for ZONE."""

    def __init__(self, session_client) -> None:
        super().__init__(session_client, "ZONE")

    def read_by_query(
            self,
            fields: Iterable[str],
            query: str = "",
            page_size: int = 100,
            offset: Optional[int] = None,
            control_id: Optional[str] = None,
    ) -> QueryResult:
        """Read ZONE records via readByQuery.

Fields (from Docs samples):
- *"""
        return super().read_by_query(
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        """Read ZONE records.

Fields (from Docs samples):
- *"""
        return super().read(keys, fields, control_id=control_id)

    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Create ZONE.

Valid fields (from Docs samples):
- ZONEDESC
- ZONEID"""
        return super().create(fields, control_id=control_id)

    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:
        """Update ZONE.

Valid fields (from Docs samples):
- RECORDNO
- ZONEDESC"""
        return super().update(fields, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        """Delete ZONE.

Key fields (from Docs samples):
- (no fields listed)"""
        return super().delete(key_field, key_value, control_id=control_id)


def _build_factory():
    class Factory(ObjectServices):
        pass

        @property
        def accttitlebyloc(self) -> AccttitlebylocService:
            """Service accessor for ACCTTITLEBYLOC."""
            return AccttitlebylocService(self._session_client)

        @property
        def accumulationtype(self) -> AccumulationtypeService:
            """Service accessor for ACCUMULATIONTYPE."""
            return AccumulationtypeService(self._session_client)

        @property
        def achbank(self) -> AchbankService:
            """Service accessor for ACHBANK."""
            return AchbankService(self._session_client)

        @property
        def activitylog(self) -> ActivitylogService:
            """Service accessor for ACTIVITYLOG."""
            return ActivitylogService(self._session_client)

        @property
        def advaudithistory(self) -> AdvaudithistoryService:
            """Service accessor for ADVAUDITHISTORY."""
            return AdvaudithistoryService(self._session_client)

        @property
        def afrsetup(self) -> AfrsetupService:
            """Service accessor for AFRSETUP."""
            return AfrsetupService(self._session_client)

        @property
        def aisle(self) -> AisleService:
            """Service accessor for AISLE."""
            return AisleService(self._session_client)

        @property
        def allocation(self) -> AllocationService:
            """Service accessor for ALLOCATION."""
            return AllocationService(self._session_client)

        @property
        def allocationentry(self) -> AllocationentryService:
            """Service accessor for ALLOCATIONENTRY."""
            return AllocationentryService(self._session_client)

        @property
        def apaccountlabel(self) -> ApaccountlabelService:
            """Service accessor for APACCOUNTLABEL."""
            return ApaccountlabelService(self._session_client)

        @property
        def apadjustment(self) -> ApadjustmentService:
            """Service accessor for APADJUSTMENT."""
            return ApadjustmentService(self._session_client)

        @property
        def apadjustmentitem(self) -> ApadjustmentitemService:
            """Service accessor for APADJUSTMENTITEM."""
            return ApadjustmentitemService(self._session_client)

        @property
        def apbill(self) -> ApbillService:
            """Service accessor for APBILL."""
            return ApbillService(self._session_client)

        @property
        def apbillbatch(self) -> ApbillbatchService:
            """Service accessor for APBILLBATCH."""
            return ApbillbatchService(self._session_client)

        @property
        def apbillitem(self) -> ApbillitemService:
            """Service accessor for APBILLITEM."""
            return ApbillitemService(self._session_client)

        @property
        def apbilljointpayee(self) -> ApbilljointpayeeService:
            """Service accessor for APBILLJOINTPAYEE."""
            return ApbilljointpayeeService(self._session_client)

        @property
        def appayment(self) -> AppaymentService:
            """Service accessor for APPAYMENT."""
            return AppaymentService(self._session_client)

        @property
        def appaymentrequest(self) -> AppaymentrequestService:
            """Service accessor for APPAYMENTREQUEST."""
            return AppaymentrequestService(self._session_client)

        @property
        def appymt(self) -> AppymtService:
            """Service accessor for APPYMT."""
            return AppymtService(self._session_client)

        @property
        def appymtdetail(self) -> AppymtdetailService:
            """Service accessor for APPYMTDETAIL."""
            return AppymtdetailService(self._session_client)

        @property
        def aprecurbill(self) -> AprecurbillService:
            """Service accessor for APRECURBILL."""
            return AprecurbillService(self._session_client)

        @property
        def aprecurbillentry(self) -> AprecurbillentryService:
            """Service accessor for APRECURBILLENTRY."""
            return AprecurbillentryService(self._session_client)

        @property
        def apretainagerelease(self) -> ApretainagereleaseService:
            """Service accessor for APRETAINAGERELEASE."""
            return ApretainagereleaseService(self._session_client)

        @property
        def apretainagereleaseentry(self) -> ApretainagereleaseentryService:
            """Service accessor for APRETAINAGERELEASEENTRY."""
            return ApretainagereleaseentryService(self._session_client)

        @property
        def apterm(self) -> AptermService:
            """Service accessor for APTERM."""
            return AptermService(self._session_client)

        @property
        def araccountlabel(self) -> AraccountlabelService:
            """Service accessor for ARACCOUNTLABEL."""
            return AraccountlabelService(self._session_client)

        @property
        def aradjustment(self) -> AradjustmentService:
            """Service accessor for ARADJUSTMENT."""
            return AradjustmentService(self._session_client)

        @property
        def aradjustmentitem(self) -> AradjustmentitemService:
            """Service accessor for ARADJUSTMENTITEM."""
            return AradjustmentitemService(self._session_client)

        @property
        def aradvance(self) -> AradvanceService:
            """Service accessor for ARADVANCE."""
            return AradvanceService(self._session_client)

        @property
        def arinvoice(self) -> ArinvoiceService:
            """Service accessor for ARINVOICE."""
            return ArinvoiceService(self._session_client)

        @property
        def arinvoicebatch(self) -> ArinvoicebatchService:
            """Service accessor for ARINVOICEBATCH."""
            return ArinvoicebatchService(self._session_client)

        @property
        def arpayment(self) -> ArpaymentService:
            """Service accessor for ARPAYMENT."""
            return ArpaymentService(self._session_client)

        @property
        def arpymt(self) -> ArpymtService:
            """Service accessor for ARPYMT."""
            return ArpymtService(self._session_client)

        @property
        def arrecurinvoice(self) -> ArrecurinvoiceService:
            """Service accessor for ARRECURINVOICE."""
            return ArrecurinvoiceService(self._session_client)

        @property
        def arrecurinvoiceentry(self) -> ArrecurinvoiceentryService:
            """Service accessor for ARRECURINVOICEENTRY."""
            return ArrecurinvoiceentryService(self._session_client)

        @property
        def arretainagerelease(self) -> ArretainagereleaseService:
            """Service accessor for ARRETAINAGERELEASE."""
            return ArretainagereleaseService(self._session_client)

        @property
        def arretainagereleaseentry(self) -> ArretainagereleaseentryService:
            """Service accessor for ARRETAINAGERELEASEENTRY."""
            return ArretainagereleaseentryService(self._session_client)

        @property
        def arterm(self) -> ArtermService:
            """Service accessor for ARTERM."""
            return ArtermService(self._session_client)

        @property
        def audithistory(self) -> AudithistoryService:
            """Service accessor for AUDITHISTORY."""
            return AudithistoryService(self._session_client)

        @property
        def availableinventory(self) -> AvailableinventoryService:
            """Service accessor for AVAILABLEINVENTORY."""
            return AvailableinventoryService(self._session_client)

        @property
        def bankacctrecon(self) -> BankacctreconService:
            """Service accessor for BANKACCTRECON."""
            return BankacctreconService(self._session_client)

        @property
        def bankaccttxnfeed(self) -> BankaccttxnfeedService:
            """Service accessor for BANKACCTTXNFEED."""
            return BankaccttxnfeedService(self._session_client)

        @property
        def bankfee(self) -> BankfeeService:
            """Service accessor for BANKFEE."""
            return BankfeeService(self._session_client)

        @property
        def bankfeeentry(self) -> BankfeeentryService:
            """Service accessor for BANKFEEENTRY."""
            return BankfeeentryService(self._session_client)

        @property
        def bin(self) -> BinService:
            """Service accessor for BIN."""
            return BinService(self._session_client)

        @property
        def binface(self) -> BinfaceService:
            """Service accessor for BINFACE."""
            return BinfaceService(self._session_client)

        @property
        def binsize(self) -> BinsizeService:
            """Service accessor for BINSIZE."""
            return BinsizeService(self._session_client)

        @property
        def cctransaction(self) -> CctransactionService:
            """Service accessor for CCTRANSACTION."""
            return CctransactionService(self._session_client)

        @property
        def cctransactionentry(self) -> CctransactionentryService:
            """Service accessor for CCTRANSACTIONENTRY."""
            return CctransactionentryService(self._session_client)

        @property
        def changerequest(self) -> ChangerequestService:
            """Service accessor for CHANGEREQUEST."""
            return ChangerequestService(self._session_client)

        @property
        def changerequestentry(self) -> ChangerequestentryService:
            """Service accessor for CHANGEREQUESTENTRY."""
            return ChangerequestentryService(self._session_client)

        @property
        def changerequeststatus(self) -> ChangerequeststatusService:
            """Service accessor for CHANGEREQUESTSTATUS."""
            return ChangerequeststatusService(self._session_client)

        @property
        def changerequesttype(self) -> ChangerequesttypeService:
            """Service accessor for CHANGEREQUESTTYPE."""
            return ChangerequesttypeService(self._session_client)

        @property
        def chargepayoff(self) -> ChargepayoffService:
            """Service accessor for CHARGEPAYOFF."""
            return ChargepayoffService(self._session_client)

        @property
        def chargepayoffentry(self) -> ChargepayoffentryService:
            """Service accessor for CHARGEPAYOFFENTRY."""
            return ChargepayoffentryService(self._session_client)

        @property
        def checkingaccount(self) -> CheckingaccountService:
            """Service accessor for CHECKINGACCOUNT."""
            return CheckingaccountService(self._session_client)

        @property
        def intacctclass(self) -> ClassService:
            """Service accessor for CLASS."""
            return ClassService(self._session_client)

        @property
        def classgroup(self) -> ClassgroupService:
            """Service accessor for CLASSGROUP."""
            return ClassgroupService(self._session_client)

        @property
        def cogsclosedje(self) -> CogsclosedjeService:
            """Service accessor for COGSCLOSEDJE."""
            return CogsclosedjeService(self._session_client)

        @property
        def compliancedefinition(self) -> CompliancedefinitionService:
            """Service accessor for COMPLIANCEDEFINITION."""
            return CompliancedefinitionService(self._session_client)

        @property
        def compliancerecord(self) -> CompliancerecordService:
            """Service accessor for COMPLIANCERECORD."""
            return CompliancerecordService(self._session_client)

        @property
        def compliancetype(self) -> CompliancetypeService:
            """Service accessor for COMPLIANCETYPE."""
            return CompliancetypeService(self._session_client)

        @property
        def contact(self) -> ContactService:
            """Service accessor for CONTACT."""
            return ContactService(self._session_client)

        @property
        def contract(self) -> ContractService:
            """Service accessor for CONTRACT."""
            return ContractService(self._session_client)

        @property
        def contractbillingschedule(self) -> ContractbillingscheduleService:
            """Service accessor for CONTRACTBILLINGSCHEDULE."""
            return ContractbillingscheduleService(self._session_client)

        @property
        def contractbillingscheduleentry(self) -> ContractbillingscheduleentryService:
            """Service accessor for CONTRACTBILLINGSCHEDULEENTRY."""
            return ContractbillingscheduleentryService(self._session_client)

        @property
        def contractbillingtemplate(self) -> ContractbillingtemplateService:
            """Service accessor for CONTRACTBILLINGTEMPLATE."""
            return ContractbillingtemplateService(self._session_client)

        @property
        def contractbillingtemplateentry(self) -> ContractbillingtemplateentryService:
            """Service accessor for CONTRACTBILLINGTEMPLATEENTRY."""
            return ContractbillingtemplateentryService(self._session_client)

        @property
        def contractdetail(self) -> ContractdetailService:
            """Service accessor for CONTRACTDETAIL."""
            return ContractdetailService(self._session_client)

        @property
        def contractexpense(self) -> ContractexpenseService:
            """Service accessor for CONTRACTEXPENSE."""
            return ContractexpenseService(self._session_client)

        @property
        def contractexpense2schedule(self) -> Contractexpense2scheduleService:
            """Service accessor for CONTRACTEXPENSE2SCHEDULE."""
            return Contractexpense2scheduleService(self._session_client)

        @property
        def contractexpenseschedule(self) -> ContractexpensescheduleService:
            """Service accessor for CONTRACTEXPENSESCHEDULE."""
            return ContractexpensescheduleService(self._session_client)

        @property
        def contractexpensetemplate(self) -> ContractexpensetemplateService:
            """Service accessor for CONTRACTEXPENSETEMPLATE."""
            return ContractexpensetemplateService(self._session_client)

        @property
        def contractgroup(self) -> ContractgroupService:
            """Service accessor for CONTRACTGROUP."""
            return ContractgroupService(self._session_client)

        @property
        def contractitemprclstentytier(self) -> ContractitemprclstentytierService:
            """Service accessor for CONTRACTITEMPRCLSTENTYTIER."""
            return ContractitemprclstentytierService(self._session_client)

        @property
        def contractitempricelist(self) -> ContractitempricelistService:
            """Service accessor for CONTRACTITEMPRICELIST."""
            return ContractitempricelistService(self._session_client)

        @property
        def contractitempricelistentry(self) -> ContractitempricelistentryService:
            """Service accessor for CONTRACTITEMPRICELISTENTRY."""
            return ContractitempricelistentryService(self._session_client)

        @property
        def contractmeabundle(self) -> ContractmeabundleService:
            """Service accessor for CONTRACTMEABUNDLE."""
            return ContractmeabundleService(self._session_client)

        @property
        def contractmeaitempricelist(self) -> ContractmeaitempricelistService:
            """Service accessor for CONTRACTMEAITEMPRICELIST."""
            return ContractmeaitempricelistService(self._session_client)

        @property
        def contractmeaitempricelistentry(self) -> ContractmeaitempricelistentryService:
            """Service accessor for CONTRACTMEAITEMPRICELISTENTRY."""
            return ContractmeaitempricelistentryService(self._session_client)

        @property
        def contractmeapricelist(self) -> ContractmeapricelistService:
            """Service accessor for CONTRACTMEAPRICELIST."""
            return ContractmeapricelistService(self._session_client)

        @property
        def contractpricelist(self) -> ContractpricelistService:
            """Service accessor for CONTRACTPRICELIST."""
            return ContractpricelistService(self._session_client)

        @property
        def contractrevenue2schedule(self) -> Contractrevenue2scheduleService:
            """Service accessor for CONTRACTREVENUE2SCHEDULE."""
            return Contractrevenue2scheduleService(self._session_client)

        @property
        def contractrevenueschedule(self) -> ContractrevenuescheduleService:
            """Service accessor for CONTRACTREVENUESCHEDULE."""
            return ContractrevenuescheduleService(self._session_client)

        @property
        def contractrevenuetemplate(self) -> ContractrevenuetemplateService:
            """Service accessor for CONTRACTREVENUETEMPLATE."""
            return ContractrevenuetemplateService(self._session_client)

        @property
        def contracttype(self) -> ContracttypeService:
            """Service accessor for CONTRACTTYPE."""
            return ContracttypeService(self._session_client)

        @property
        def contractusage(self) -> ContractusageService:
            """Service accessor for CONTRACTUSAGE."""
            return ContractusageService(self._session_client)

        @property
        def costtype(self) -> CosttypeService:
            """Service accessor for COSTTYPE."""
            return CosttypeService(self._session_client)

        @property
        def creditcard(self) -> CreditcardService:
            """Service accessor for CREDITCARD."""
            return CreditcardService(self._session_client)

        @property
        def creditcardfee(self) -> CreditcardfeeService:
            """Service accessor for CREDITCARDFEE."""
            return CreditcardfeeService(self._session_client)

        @property
        def creditcardfeeentry(self) -> CreditcardfeeentryService:
            """Service accessor for CREDITCARDFEEENTRY."""
            return CreditcardfeeentryService(self._session_client)

        @property
        def customer(self) -> CustomerService:
            """Service accessor for CUSTOMER."""
            return CustomerService(self._session_client)

        @property
        def customeremailtemplate(self) -> CustomeremailtemplateService:
            """Service accessor for CUSTOMEREMAILTEMPLATE."""
            return CustomeremailtemplateService(self._session_client)

        @property
        def customergroup(self) -> CustomergroupService:
            """Service accessor for CUSTOMERGROUP."""
            return CustomergroupService(self._session_client)

        @property
        def customervisibility(self) -> CustomervisibilityService:
            """Service accessor for CUSTOMERVISIBILITY."""
            return CustomervisibilityService(self._session_client)

        @property
        def custtype(self) -> CusttypeService:
            """Service accessor for CUSTTYPE."""
            return CusttypeService(self._session_client)

        @property
        def ddsjob(self) -> DdsjobService:
            """Service accessor for DDSJOB."""
            return DdsjobService(self._session_client)

        @property
        def department(self) -> DepartmentService:
            """Service accessor for DEPARTMENT."""
            return DepartmentService(self._session_client)

        @property
        def departmentgroup(self) -> DepartmentgroupService:
            """Service accessor for DEPARTMENTGROUP."""
            return DepartmentgroupService(self._session_client)

        @property
        def deposit(self) -> DepositService:
            """Service accessor for DEPOSIT."""
            return DepositService(self._session_client)

        @property
        def depositentry(self) -> DepositentryService:
            """Service accessor for DEPOSITENTRY."""
            return DepositentryService(self._session_client)

        @property
        def dunningdefinition(self) -> DunningdefinitionService:
            """Service accessor for DUNNINGDEFINITION."""
            return DunningdefinitionService(self._session_client)

        @property
        def earningtype(self) -> EarningtypeService:
            """Service accessor for EARNINGTYPE."""
            return EarningtypeService(self._session_client)

        @property
        def eeaccountlabel(self) -> EeaccountlabelService:
            """Service accessor for EEACCOUNTLABEL."""
            return EeaccountlabelService(self._session_client)

        @property
        def eexpenses(self) -> EexpensesService:
            """Service accessor for EEXPENSES."""
            return EexpensesService(self._session_client)

        @property
        def employee(self) -> EmployeeService:
            """Service accessor for EMPLOYEE."""
            return EmployeeService(self._session_client)

        @property
        def employeegroup(self) -> EmployeegroupService:
            """Service accessor for EMPLOYEEGROUP."""
            return EmployeegroupService(self._session_client)

        @property
        def employeeposition(self) -> EmployeepositionService:
            """Service accessor for EMPLOYEEPOSITION."""
            return EmployeepositionService(self._session_client)

        @property
        def employeetype(self) -> EmployeetypeService:
            """Service accessor for EMPLOYEETYPE."""
            return EmployeetypeService(self._session_client)

        @property
        def eppayment(self) -> EppaymentService:
            """Service accessor for EPPAYMENT."""
            return EppaymentService(self._session_client)

        @property
        def eppaymentrequest(self) -> EppaymentrequestService:
            """Service accessor for EPPAYMENTREQUEST."""
            return EppaymentrequestService(self._session_client)

        @property
        def exchangerate(self) -> ExchangerateService:
            """Service accessor for EXCHANGERATE."""
            return ExchangerateService(self._session_client)

        @property
        def exchangerateentry(self) -> ExchangerateentryService:
            """Service accessor for EXCHANGERATEENTRY."""
            return ExchangerateentryService(self._session_client)

        @property
        def exchangeratetypes(self) -> ExchangeratetypesService:
            """Service accessor for EXCHANGERATETYPES."""
            return ExchangeratetypesService(self._session_client)

        @property
        def expenseadjustments(self) -> ExpenseadjustmentsService:
            """Service accessor for EXPENSEADJUSTMENTS."""
            return ExpenseadjustmentsService(self._session_client)

        @property
        def expenseadjustmentsitem(self) -> ExpenseadjustmentsitemService:
            """Service accessor for EXPENSEADJUSTMENTSITEM."""
            return ExpenseadjustmentsitemService(self._session_client)

        @property
        def expensepaymenttype(self) -> ExpensepaymenttypeService:
            """Service accessor for EXPENSEPAYMENTTYPE."""
            return ExpensepaymenttypeService(self._session_client)

        @property
        def fundstransfer(self) -> FundstransferService:
            """Service accessor for FUNDSTRANSFER."""
            return FundstransferService(self._session_client)

        @property
        def fundstransferentry(self) -> FundstransferentryService:
            """Service accessor for FUNDSTRANSFERENTRY."""
            return FundstransferentryService(self._session_client)

        @property
        def gcbook(self) -> GcbookService:
            """Service accessor for GCBOOK."""
            return GcbookService(self._session_client)

        @property
        def gcbookacctratetype(self) -> GcbookacctratetypeService:
            """Service accessor for GCBOOKACCTRATETYPE."""
            return GcbookacctratetypeService(self._session_client)

        @property
        def gcbookadjjournal(self) -> GcbookadjjournalService:
            """Service accessor for GCBOOKADJJOURNAL."""
            return GcbookadjjournalService(self._session_client)

        @property
        def gcbookelimaccount(self) -> GcbookelimaccountService:
            """Service accessor for GCBOOKELIMACCOUNT."""
            return GcbookelimaccountService(self._session_client)

        @property
        def gcbookentity(self) -> GcbookentityService:
            """Service accessor for GCBOOKENTITY."""
            return GcbookentityService(self._session_client)

        @property
        def gcownershipchildentity(self) -> GcownershipchildentityService:
            """Service accessor for GCOWNERSHIPCHILDENTITY."""
            return GcownershipchildentityService(self._session_client)

        @property
        def gcownershipentity(self) -> GcownershipentityService:
            """Service accessor for GCOWNERSHIPENTITY."""
            return GcownershipentityService(self._session_client)

        @property
        def gcownershipstructure(self) -> GcownershipstructureService:
            """Service accessor for GCOWNERSHIPSTRUCTURE."""
            return GcownershipstructureService(self._session_client)

        @property
        def gcownershipstructuredetail(self) -> GcownershipstructuredetailService:
            """Service accessor for GCOWNERSHIPSTRUCTUREDETAIL."""
            return GcownershipstructuredetailService(self._session_client)

        @property
        def geninvoicepolicy(self) -> GeninvoicepolicyService:
            """Service accessor for GENINVOICEPOLICY."""
            return GeninvoicepolicyService(self._session_client)

        @property
        def geninvoicepreview(self) -> GeninvoicepreviewService:
            """Service accessor for GENINVOICEPREVIEW."""
            return GeninvoicepreviewService(self._session_client)

        @property
        def geninvoicepreviewline(self) -> GeninvoicepreviewlineService:
            """Service accessor for GENINVOICEPREVIEWLINE."""
            return GeninvoicepreviewlineService(self._session_client)

        @property
        def geninvoicerun(self) -> GeninvoicerunService:
            """Service accessor for GENINVOICERUN."""
            return GeninvoicerunService(self._session_client)

        @property
        def glaccount(self) -> GlaccountService:
            """Service accessor for GLACCOUNT."""
            return GlaccountService(self._session_client)

        @property
        def glaccountbalance(self) -> GlaccountbalanceService:
            """Service accessor for GLACCOUNTBALANCE."""
            return GlaccountbalanceService(self._session_client)

        @property
        def glacctallocation(self) -> GlacctallocationService:
            """Service accessor for GLACCTALLOCATION."""
            return GlacctallocationService(self._session_client)

        @property
        def glacctallocationgrp(self) -> GlacctallocationgrpService:
            """Service accessor for GLACCTALLOCATIONGRP."""
            return GlacctallocationgrpService(self._session_client)

        @property
        def glacctallocationrun(self) -> GlacctallocationrunService:
            """Service accessor for GLACCTALLOCATIONRUN."""
            return GlacctallocationrunService(self._session_client)

        @property
        def glacctgrp(self) -> GlacctgrpService:
            """Service accessor for GLACCTGRP."""
            return GlacctgrpService(self._session_client)

        @property
        def glacctgrphierarchy(self) -> GlacctgrphierarchyService:
            """Service accessor for GLACCTGRPHIERARCHY."""
            return GlacctgrphierarchyService(self._session_client)

        @property
        def glacctgrppurpose(self) -> GlacctgrppurposeService:
            """Service accessor for GLACCTGRPPURPOSE."""
            return GlacctgrppurposeService(self._session_client)

        @property
        def glbatch(self) -> GlbatchService:
            """Service accessor for GLBATCH."""
            return GlbatchService(self._session_client)

        @property
        def glbudgetheader(self) -> GlbudgetheaderService:
            """Service accessor for GLBUDGETHEADER."""
            return GlbudgetheaderService(self._session_client)

        @property
        def glbudgetitem(self) -> GlbudgetitemService:
            """Service accessor for GLBUDGETITEM."""
            return GlbudgetitemService(self._session_client)

        @property
        def gldetail(self) -> GldetailService:
            """Service accessor for GLDETAIL."""
            return GldetailService(self._session_client)

        @property
        def glentry(self) -> GlentryService:
            """Service accessor for GLENTRY."""
            return GlentryService(self._session_client)

        @property
        def iccyclecount(self) -> IccyclecountService:
            """Service accessor for ICCYCLECOUNT."""
            return IccyclecountService(self._session_client)

        @property
        def iccyclecountentry(self) -> IccyclecountentryService:
            """Service accessor for ICCYCLECOUNTENTRY."""
            return IccyclecountentryService(self._session_client)

        @property
        def icrow(self) -> IcrowService:
            """Service accessor for ICROW."""
            return IcrowService(self._session_client)

        @property
        def ictransfer(self) -> IctransferService:
            """Service accessor for ICTRANSFER."""
            return IctransferService(self._session_client)

        @property
        def interentitysetup(self) -> InterentitysetupService:
            """Service accessor for INTERENTITYSETUP."""
            return InterentitysetupService(self._session_client)

        @property
        def invdocument(self) -> InvdocumentService:
            """Service accessor for INVDOCUMENT."""
            return InvdocumentService(self._session_client)

        @property
        def invdocumententry(self) -> InvdocumententryService:
            """Service accessor for INVDOCUMENTENTRY."""
            return InvdocumententryService(self._session_client)

        @property
        def invdocumentparams(self) -> InvdocumentparamsService:
            """Service accessor for INVDOCUMENTPARAMS."""
            return InvdocumentparamsService(self._session_client)

        @property
        def invdocumentsubtotals(self) -> InvdocumentsubtotalsService:
            """Service accessor for INVDOCUMENTSUBTOTALS."""
            return InvdocumentsubtotalsService(self._session_client)

        @property
        def inventorytotaldetail(self) -> InventorytotaldetailService:
            """Service accessor for INVENTORYTOTALDETAIL."""
            return InventorytotaldetailService(self._session_client)

        @property
        def inventorywqdetail(self) -> InventorywqdetailService:
            """Service accessor for INVENTORYWQDETAIL."""
            return InventorywqdetailService(self._session_client)

        @property
        def inventorywqorder(self) -> InventorywqorderService:
            """Service accessor for INVENTORYWQORDER."""
            return InventorywqorderService(self._session_client)

        @property
        def invpricelist(self) -> InvpricelistService:
            """Service accessor for INVPRICELIST."""
            return InvpricelistService(self._session_client)

        @property
        def item(self) -> ItemService:
            """Service accessor for ITEM."""
            return ItemService(self._session_client)

        @property
        def itemcrossref(self) -> ItemcrossrefService:
            """Service accessor for ITEMCROSSREF."""
            return ItemcrossrefService(self._session_client)

        @property
        def itemglgroup(self) -> ItemglgroupService:
            """Service accessor for ITEMGLGROUP."""
            return ItemglgroupService(self._session_client)

        @property
        def itemgroup(self) -> ItemgroupService:
            """Service accessor for ITEMGROUP."""
            return ItemgroupService(self._session_client)

        @property
        def itemtaxgroup(self) -> ItemtaxgroupService:
            """Service accessor for ITEMTAXGROUP."""
            return ItemtaxgroupService(self._session_client)

        @property
        def itemwarehouseinfo(self) -> ItemwarehouseinfoService:
            """Service accessor for ITEMWAREHOUSEINFO."""
            return ItemwarehouseinfoService(self._session_client)

        @property
        def jobqueuerecord(self) -> JobqueuerecordService:
            """Service accessor for JOBQUEUERECORD."""
            return JobqueuerecordService(self._session_client)

        @property
        def laborclass(self) -> LaborclassService:
            """Service accessor for LABORCLASS."""
            return LaborclassService(self._session_client)

        @property
        def laborshift(self) -> LaborshiftService:
            """Service accessor for LABORSHIFT."""
            return LaborshiftService(self._session_client)

        @property
        def laborunion(self) -> LaborunionService:
            """Service accessor for LABORUNION."""
            return LaborunionService(self._session_client)

        @property
        def location(self) -> LocationService:
            """Service accessor for LOCATION."""
            return LocationService(self._session_client)

        @property
        def locationentity(self) -> LocationentityService:
            """Service accessor for LOCATIONENTITY."""
            return LocationentityService(self._session_client)

        @property
        def locationgroup(self) -> LocationgroupService:
            """Service accessor for LOCATIONGROUP."""
            return LocationgroupService(self._session_client)

        @property
        def memberusergroup(self) -> MemberusergroupService:
            """Service accessor for MEMBERUSERGROUP."""
            return MemberusergroupService(self._session_client)

        @property
        def obspctcompleted(self) -> ObspctcompletedService:
            """Service accessor for OBSPCTCOMPLETED."""
            return ObspctcompletedService(self._session_client)

        @property
        def otherreceipts(self) -> OtherreceiptsService:
            """Service accessor for OTHERRECEIPTS."""
            return OtherreceiptsService(self._session_client)

        @property
        def otherreceiptsentry(self) -> OtherreceiptsentryService:
            """Service accessor for OTHERRECEIPTSENTRY."""
            return OtherreceiptsentryService(self._session_client)

        @property
        def payrollreportcheck(self) -> PayrollreportcheckService:
            """Service accessor for PAYROLLREPORTCHECK."""
            return PayrollreportcheckService(self._session_client)

        @property
        def payrollreportemployee(self) -> PayrollreportemployeeService:
            """Service accessor for PAYROLLREPORTEMPLOYEE."""
            return PayrollreportemployeeService(self._session_client)

        @property
        def payrollreportgrosspay(self) -> PayrollreportgrosspayService:
            """Service accessor for PAYROLLREPORTGROSSPAY."""
            return PayrollreportgrosspayService(self._session_client)

        @property
        def payrollreportpaymodifier(self) -> PayrollreportpaymodifierService:
            """Service accessor for PAYROLLREPORTPAYMODIFIER."""
            return PayrollreportpaymodifierService(self._session_client)

        @property
        def payrollreportptoaccrualschedule(self) -> PayrollreportptoaccrualscheduleService:
            """Service accessor for PAYROLLREPORTPTOACCRUALSCHEDULE."""
            return PayrollreportptoaccrualscheduleService(self._session_client)

        @property
        def payrollreportptoactivity(self) -> PayrollreportptoactivityService:
            """Service accessor for PAYROLLREPORTPTOACTIVITY."""
            return PayrollreportptoactivityService(self._session_client)

        @property
        def payrollreporttax(self) -> PayrollreporttaxService:
            """Service accessor for PAYROLLREPORTTAX."""
            return PayrollreporttaxService(self._session_client)

        @property
        def payrollreporttaxsetup(self) -> PayrollreporttaxsetupService:
            """Service accessor for PAYROLLREPORTTAXSETUP."""
            return PayrollreporttaxsetupService(self._session_client)

        @property
        def payrollreporttimecard(self) -> PayrollreporttimecardService:
            """Service accessor for PAYROLLREPORTTIMECARD."""
            return PayrollreporttimecardService(self._session_client)

        @property
        def payrollreporttrade(self) -> PayrollreporttradeService:
            """Service accessor for PAYROLLREPORTTRADE."""
            return PayrollreporttradeService(self._session_client)

        @property
        def pjestimate(self) -> PjestimateService:
            """Service accessor for PJESTIMATE."""
            return PjestimateService(self._session_client)

        @property
        def pjestimateentry(self) -> PjestimateentryService:
            """Service accessor for PJESTIMATEENTRY."""
            return PjestimateentryService(self._session_client)

        @property
        def pjestimatetype(self) -> PjestimatetypeService:
            """Service accessor for PJESTIMATETYPE."""
            return PjestimatetypeService(self._session_client)

        @property
        def podocument(self) -> PodocumentService:
            """Service accessor for PODOCUMENT."""
            return PodocumentService(self._session_client)

        @property
        def podocumententry(self) -> PodocumententryService:
            """Service accessor for PODOCUMENTENTRY."""
            return PodocumententryService(self._session_client)

        @property
        def podocumentparams(self) -> PodocumentparamsService:
            """Service accessor for PODOCUMENTPARAMS."""
            return PodocumentparamsService(self._session_client)

        @property
        def podocumentsubtotals(self) -> PodocumentsubtotalsService:
            """Service accessor for PODOCUMENTSUBTOTALS."""
            return PodocumentsubtotalsService(self._session_client)

        @property
        def popricelist(self) -> PopricelistService:
            """Service accessor for POPRICELIST."""
            return PopricelistService(self._session_client)

        @property
        def positionskill(self) -> PositionskillService:
            """Service accessor for POSITIONSKILL."""
            return PositionskillService(self._session_client)

        @property
        def posubtotaltemplate(self) -> PosubtotaltemplateService:
            """Service accessor for POSUBTOTALTEMPLATE."""
            return PosubtotaltemplateService(self._session_client)

        @property
        def productline(self) -> ProductlineService:
            """Service accessor for PRODUCTLINE."""
            return ProductlineService(self._session_client)

        @property
        def project(self) -> ProjectService:
            """Service accessor for PROJECT."""
            return ProjectService(self._session_client)

        @property
        def projectchangeorder(self) -> ProjectchangeorderService:
            """Service accessor for PROJECTCHANGEORDER."""
            return ProjectchangeorderService(self._session_client)

        @property
        def projectcontract(self) -> ProjectcontractService:
            """Service accessor for PROJECTCONTRACT."""
            return ProjectcontractService(self._session_client)

        @property
        def projectcontractline(self) -> ProjectcontractlineService:
            """Service accessor for PROJECTCONTRACTLINE."""
            return ProjectcontractlineService(self._session_client)

        @property
        def projectcontractlineentry(self) -> ProjectcontractlineentryService:
            """Service accessor for PROJECTCONTRACTLINEENTRY."""
            return ProjectcontractlineentryService(self._session_client)

        @property
        def projectcontracttype(self) -> ProjectcontracttypeService:
            """Service accessor for PROJECTCONTRACTTYPE."""
            return ProjectcontracttypeService(self._session_client)

        @property
        def projectgroup(self) -> ProjectgroupService:
            """Service accessor for PROJECTGROUP."""
            return ProjectgroupService(self._session_client)

        @property
        def projectresources(self) -> ProjectresourcesService:
            """Service accessor for PROJECTRESOURCES."""
            return ProjectresourcesService(self._session_client)

        @property
        def projectstatus(self) -> ProjectstatusService:
            """Service accessor for PROJECTSTATUS."""
            return ProjectstatusService(self._session_client)

        @property
        def projecttype(self) -> ProjecttypeService:
            """Service accessor for PROJECTTYPE."""
            return ProjecttypeService(self._session_client)

        @property
        def providerbankaccount(self) -> ProviderbankaccountService:
            """Service accessor for PROVIDERBANKACCOUNT."""
            return ProviderbankaccountService(self._session_client)

        @property
        def providerpaymentmethod(self) -> ProviderpaymentmethodService:
            """Service accessor for PROVIDERPAYMENTMETHOD."""
            return ProviderpaymentmethodService(self._session_client)

        @property
        def providervendor(self) -> ProvidervendorService:
            """Service accessor for PROVIDERVENDOR."""
            return ProvidervendorService(self._session_client)

        @property
        def ptapplication(self) -> PtapplicationService:
            """Service accessor for PTAPPLICATION."""
            return PtapplicationService(self._session_client)

        @property
        def ratetable(self) -> RatetableService:
            """Service accessor for RATETABLE."""
            return RatetableService(self._session_client)

        @property
        def ratetableapentry(self) -> RatetableapentryService:
            """Service accessor for RATETABLEAPENTRY."""
            return RatetableapentryService(self._session_client)

        @property
        def ratetablepoentry(self) -> RatetablepoentryService:
            """Service accessor for RATETABLEPOENTRY."""
            return RatetablepoentryService(self._session_client)

        @property
        def ratetabletsentry(self) -> RatetabletsentryService:
            """Service accessor for RATETABLETSENTRY."""
            return RatetabletsentryService(self._session_client)

        @property
        def recurglacctallocation(self) -> RecurglacctallocationService:
            """Service accessor for RECURGLACCTALLOCATION."""
            return RecurglacctallocationService(self._session_client)

        @property
        def reportingperiod(self) -> ReportingperiodService:
            """Service accessor for REPORTINGPERIOD."""
            return ReportingperiodService(self._session_client)

        @property
        def revrecschedule(self) -> RevrecscheduleService:
            """Service accessor for REVRECSCHEDULE."""
            return RevrecscheduleService(self._session_client)

        @property
        def revrecscheduleentry(self) -> RevrecscheduleentryService:
            """Service accessor for REVRECSCHEDULEENTRY."""
            return RevrecscheduleentryService(self._session_client)

        @property
        def roleassignment(self) -> RoleassignmentService:
            """Service accessor for ROLEASSIGNMENT."""
            return RoleassignmentService(self._session_client)

        @property
        def rolegroups(self) -> RolegroupsService:
            """Service accessor for ROLEGROUPS."""
            return RolegroupsService(self._session_client)

        @property
        def rolepolicyassignment(self) -> RolepolicyassignmentService:
            """Service accessor for ROLEPOLICYASSIGNMENT."""
            return RolepolicyassignmentService(self._session_client)

        @property
        def roles(self) -> RolesService:
            """Service accessor for ROLES."""
            return RolesService(self._session_client)

        @property
        def roleusers(self) -> RoleusersService:
            """Service accessor for ROLEUSERS."""
            return RoleusersService(self._session_client)

        @property
        def savingsaccount(self) -> SavingsaccountService:
            """Service accessor for SAVINGSACCOUNT."""
            return SavingsaccountService(self._session_client)

        @property
        def sodocument(self) -> SodocumentService:
            """Service accessor for SODOCUMENT."""
            return SodocumentService(self._session_client)

        @property
        def sodocumententry(self) -> SodocumententryService:
            """Service accessor for SODOCUMENTENTRY."""
            return SodocumententryService(self._session_client)

        @property
        def sodocumentparams(self) -> SodocumentparamsService:
            """Service accessor for SODOCUMENTPARAMS."""
            return SodocumentparamsService(self._session_client)

        @property
        def sodocumentsubtotals(self) -> SodocumentsubtotalsService:
            """Service accessor for SODOCUMENTSUBTOTALS."""
            return SodocumentsubtotalsService(self._session_client)

        @property
        def sopricelist(self) -> SopricelistService:
            """Service accessor for SOPRICELIST."""
            return SopricelistService(self._session_client)

        @property
        def sorecurdocument(self) -> SorecurdocumentService:
            """Service accessor for SORECURDOCUMENT."""
            return SorecurdocumentService(self._session_client)

        @property
        def sosubtotaltemplate(self) -> SosubtotaltemplateService:
            """Service accessor for SOSUBTOTALTEMPLATE."""
            return SosubtotaltemplateService(self._session_client)

        @property
        def standardcosttype(self) -> StandardcosttypeService:
            """Service accessor for STANDARDCOSTTYPE."""
            return StandardcosttypeService(self._session_client)

        @property
        def standardtask(self) -> StandardtaskService:
            """Service accessor for STANDARDTASK."""
            return StandardtaskService(self._session_client)

        @property
        def stataccount(self) -> StataccountService:
            """Service accessor for STATACCOUNT."""
            return StataccountService(self._session_client)

        @property
        def task(self) -> TaskService:
            """Service accessor for TASK."""
            return TaskService(self._session_client)

        @property
        def taskresources(self) -> TaskresourcesService:
            """Service accessor for TASKRESOURCES."""
            return TaskresourcesService(self._session_client)

        @property
        def taxdetail(self) -> TaxdetailService:
            """Service accessor for TAXDETAIL."""
            return TaxdetailService(self._session_client)

        @property
        def taxrecord(self) -> TaxrecordService:
            """Service accessor for TAXRECORD."""
            return TaxrecordService(self._session_client)

        @property
        def taxsolution(self) -> TaxsolutionService:
            """Service accessor for TAXSOLUTION."""
            return TaxsolutionService(self._session_client)

        @property
        def timesheet(self) -> TimesheetService:
            """Service accessor for TIMESHEET."""
            return TimesheetService(self._session_client)

        @property
        def timesheetapproval(self) -> TimesheetapprovalService:
            """Service accessor for TIMESHEETAPPROVAL."""
            return TimesheetapprovalService(self._session_client)

        @property
        def timesheetentry(self) -> TimesheetentryService:
            """Service accessor for TIMESHEETENTRY."""
            return TimesheetentryService(self._session_client)

        @property
        def timetype(self) -> TimetypeService:
            """Service accessor for TIMETYPE."""
            return TimetypeService(self._session_client)

        @property
        def transactionrule(self) -> TransactionruleService:
            """Service accessor for TRANSACTIONRULE."""
            return TransactionruleService(self._session_client)

        @property
        def transactionruledetail(self) -> TransactionruledetailService:
            """Service accessor for TRANSACTIONRULEDETAIL."""
            return TransactionruledetailService(self._session_client)

        @property
        def uom(self) -> UomService:
            """Service accessor for UOM."""
            return UomService(self._session_client)

        @property
        def uomdetail(self) -> UomdetailService:
            """Service accessor for UOMDETAIL."""
            return UomdetailService(self._session_client)

        @property
        def usergroup(self) -> UsergroupService:
            """Service accessor for USERGROUP."""
            return UsergroupService(self._session_client)

        @property
        def userinfo(self) -> UserinfoService:
            """Service accessor for USERINFO."""
            return UserinfoService(self._session_client)

        @property
        def userrestriction(self) -> UserrestrictionService:
            """Service accessor for USERRESTRICTION."""
            return UserrestrictionService(self._session_client)

        @property
        def userrights(self) -> UserrightsService:
            """Service accessor for USERRIGHTS."""
            return UserrightsService(self._session_client)

        @property
        def userroles(self) -> UserrolesService:
            """Service accessor for USERROLES."""
            return UserrolesService(self._session_client)

        @property
        def vendor(self) -> VendorService:
            """Service accessor for VENDOR."""
            return VendorService(self._session_client)

        @property
        def vendoremailtemplate(self) -> VendoremailtemplateService:
            """Service accessor for VENDOREMAILTEMPLATE."""
            return VendoremailtemplateService(self._session_client)

        @property
        def vendorgroup(self) -> VendorgroupService:
            """Service accessor for VENDORGROUP."""
            return VendorgroupService(self._session_client)

        @property
        def vendorvisibility(self) -> VendorvisibilityService:
            """Service accessor for VENDORVISIBILITY."""
            return VendorvisibilityService(self._session_client)

        @property
        def vendtype(self) -> VendtypeService:
            """Service accessor for VENDTYPE."""
            return VendtypeService(self._session_client)

        @property
        def warehouse(self) -> WarehouseService:
            """Service accessor for WAREHOUSE."""
            return WarehouseService(self._session_client)

        @property
        def warehousegroup(self) -> WarehousegroupService:
            """Service accessor for WAREHOUSEGROUP."""
            return WarehousegroupService(self._session_client)

        @property
        def zone(self) -> ZoneService:
            """Service accessor for ZONE."""
            return ZoneService(self._session_client)

    return Factory


ObjectServices = _build_factory()
