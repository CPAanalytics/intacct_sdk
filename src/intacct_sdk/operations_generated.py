from __future__ import annotations

from typing import Optional, Dict

from . import xml as xml_builder
from .models import ResultData


class OperationMixin:
    def execute(
        self,
        operation: str,
        payload: Optional[xml_builder.Payload] = None,
        operation_attrs: Optional[Dict[str, str]] = None,
        control_id: Optional[str] = None,
    ) -> ResultData:
        raise NotImplementedError

    def apply_arpayment(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "apply_arpayment".
        
        Fields (from Docs samples):
        - arpaymentitems.arpaymentitem.amount
        - arpaymentitems.arpaymentitem.invoicekey
        - arpaymentkey
        - memo
        - overpaydeptid
        - overpaylocid
        - paymentdate.day
        - paymentdate.month
        - paymentdate.year"""
        return self.execute("apply_arpayment", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def approve(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "approve".
        
        Fields (from Docs samples):
        - PODOCUMENT.COMMENT
        - PODOCUMENT.DOCID
        - TIMESHEET.COMMENT
        - TIMESHEET.RECORDNO"""
        return self.execute("approve", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def approve_appaymentrequest(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "approve_appaymentrequest".
        
        Fields (from Docs samples):
        - appaymentkeys.appaymentkey"""
        return self.execute("approve_appaymentrequest", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def approve_vendor(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "approveVendor".
        
        Fields (from Docs samples):
        - recordno
        - reviewcomments"""
        return self.execute("approveVendor", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def cancel(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "cancel".
        
        Fields (from Docs samples):
        - JOBQUEUERECORD.JOBID"""
        return self.execute("cancel", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def clearallmea(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "clearallmea".
        
        Fields (from Docs samples):
        - CONTRACT.CONTRACTID"""
        return self.execute("clearallmea", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def clearlastactivemea(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "clearlastactivemea".
        
        Fields (from Docs samples):
        - CONTRACT.CONTRACTID"""
        return self.execute("clearlastactivemea", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def confirm_appaymentrequest(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "confirm_appaymentrequest".
        
        Fields (from Docs samples):
        - appaymentkeys.appaymentkey"""
        return self.execute("confirm_appaymentrequest", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def consolidate(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "consolidate".
        
        Fields (from Docs samples):
        - bookid
        - changesonly
        - email
        - entities.csnentity.bsrate
        - entities.csnentity.entityid
        - entities.csnentity.warate
        - offline
        - reportingperiodname
        - updatesucceedingperiods"""
        return self.execute("consolidate", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def consolidatebytier(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "consolidatebytier".
        
        Fields (from Docs samples):
        - email
        - reportingperiodname
        - structurename"""
        return self.execute("consolidatebytier", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create".
        
        Fields (from Docs samples):
        - ACCUMULATIONTYPE:
          - NAME
        - AFRSETUP:
          - DISABLEDELETE
          - DISABLEEDIT
          - DISABLERECLASS
        - ALLOCATION:
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
          - TYPE
        - APACCOUNTLABEL:
          - ACCOUNTLABEL
          - DESCRIPTION
          - GLACCOUNTNO
          - OFFSETGLACCOUNTNO
          - STATUS
        - APBILL:
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
          - WHENPOSTED
        - APBILLJOINTPAYEE:
          - APBILLKEY
          - JOINTPAYEENAME
          - JOINTPAYEEPRINTAS
        - APPYMT:
          - APPYMTDETAILS.APPYMTDETAIL.RECORDKEY
          - APPYMTDETAILS.APPYMTDETAIL.TRX_PAYMENTAMOUNT
          - FINANCIALENTITY
          - PAYMENTDATE
          - PAYMENTMETHOD
          - VENDORID
        - APRETAINAGERELEASE:
          - APRETAINAGERELEASEENTRIES.APRETAINAGERELEASEENTRY.RETAINAGEBILLITEMKEY
          - APRETAINAGERELEASEENTRIES.APRETAINAGERELEASEENTRY.RETAINAGEBILLKEY
          - APRETAINAGERELEASEENTRIES.APRETAINAGERELEASEENTRY.TRX_AMOUNTRELEASED
          - DESCRIPTION
          - RELEASEDATE
        - ARACCOUNTLABEL:
          - ACCOUNTLABEL
          - DESCRIPTION
          - GLACCOUNTNO
          - OFFSETGLACCOUNTNO
          - STATUS
        - ARADVANCE:
          - ARADVANCEITEMS.ARADVANCEITEM.ACCOUNTLABEL
          - ARADVANCEITEMS.ARADVANCEITEM.TRX_AMOUNT
          - CUSTOMERID
          - PAYMENTDATE
          - PAYMENTMETHOD
          - RECEIPTDATE
          - UNDEPOSITEDACCOUNTNO
        - ARPYMT:
          - ARPYMTDETAILS.ARPYMTDETAIL.RECORDKEY
          - ARPYMTDETAILS.ARPYMTDETAIL.TRX_PAYMENTAMOUNT
          - CUSTOMERID
          - DOCNUMBER
          - FINANCIALENTITY
          - PAYMENTDATE
          - PAYMENTMETHOD
          - RECEIPTDATE
        - ARRETAINAGERELEASE:
          - ARRETAINAGERELEASEENTRIES.ARRETAINAGERELEASEENTRY.RETAINAGEINVOICEITEMKEY
          - ARRETAINAGERELEASEENTRIES.ARRETAINAGERELEASEENTRY.RETAINAGEINVOICEKEY
          - ARRETAINAGERELEASEENTRIES.ARRETAINAGERELEASEENTRY.TRX_AMOUNTRELEASED
          - DESCRIPTION
          - RELEASEDATE
        - BANKACCTRECON:
          - CUTOFFDATE
          - FINANCIALENTITY
          - MODE
          - STMTENDINGBALANCE
          - STMTENDINGDATE
        - BANKACCTTXNFEED:
          - BANKACCTTXNRECORDS.BANKACCTTXNRECORD.AMOUNT
          - BANKACCTTXNRECORDS.BANKACCTTXNRECORD.DESCRIPTION
          - BANKACCTTXNRECORDS.BANKACCTTXNRECORD.DOCNO
          - BANKACCTTXNRECORDS.BANKACCTTXNRECORD.DOCTYPE
          - BANKACCTTXNRECORDS.BANKACCTTXNRECORD.POSTINGDATE
          - BANKACCTTXNRECORDS.BANKACCTTXNRECORD.TRANSACTIONTYPE
          - FEEDDATE
          - FEEDTYPE
          - FINANCIALENTITY
        - BIN:
          - AISLEID
          - BINDESC
          - BINID
          - BINSIZEID
          - FACEID
          - ROWID
          - WAREHOUSEID
          - ZONEID
        - BINFACE:
          - FACEDESC
          - FACEID
        - BINSIZE:
          - SIZEDESC
          - SIZEID
        - CHANGEREQUEST:
          - CHANGEREQUESTDATE
          - CHANGEREQUESTENTRIES.CHANGEREQUESTENTRY.COST
          - CHANGEREQUESTENTRIES.CHANGEREQUESTENTRY.COSTTYPEID
          - CHANGEREQUESTENTRIES.CHANGEREQUESTENTRY.PRICE
          - CHANGEREQUESTENTRIES.CHANGEREQUESTENTRY.PROJECTID
          - CHANGEREQUESTENTRIES.CHANGEREQUESTENTRY.TASKID
          - CHANGEREQUESTID
          - PROJECTID
        - CHANGEREQUESTSTATUS:
          - NAME
          - WFTYPE
        - CHANGEREQUESTTYPE:
          - NAME
        - CLASS:
          - CLASSID
          - NAME
        - COMPLIANCEDEFINITION:
          - CATEGORY
          - COMPDEFENTRIES.VENDTYPENAME
          - COMPLIANCEDEFINITIONID
          - DESCRIPTION
          - GENERATERULE
          - NAME
          - PAYMENTNOTIFICATION
          - TRACKBY
          - VALIDATIONRULE
        - COMPLIANCERECORD:
          - COMPLIANCETYPEID
          - NAME
          - NOTES
          - PROJECTID
          - VENDORID
        - COMPLIANCETYPE:
          - COMPLIANCEDEFINITIONID
          - COMPLIANCETYPEID
          - NAME
          - SEQNUMID
        - CONTACT:
          - CONTACTNAME
          - PRINTAS
        - CONTRACT:
          - BEGINDATE
          - BILLINGFREQUENCY
          - CONTRACTID
          - CURRENCY
          - CUSTOMERID
          - ENDDATE
          - EXCHRATETYPE
          - LOCATIONID
          - NAME
          - TERMNAME
        - CONTRACTBILLINGTEMPLATE:
          - CONTRACTBILLINGTEMPLATEENTRIES.CONTRACTBILLINGTEMPLATEENTRY.PERCENTBILLED
          - CONTRACTBILLINGTEMPLATEENTRIES.CONTRACTBILLINGTEMPLATEENTRY.PERIODOFFSET
          - DESCRIPTION
          - METHOD
          - NAME
        - CONTRACTDETAIL:
          - BEGINDATE
          - BILLINGMETHOD
          - BILLINGOPTIONS
          - BILLINGTEMPLATENAME
          - CONTRACTID
          - ENDDATE
          - FLATAMOUNT
          - ITEMID
          - LOCATIONID
          - REVENUETEMPLATENAME
        - CONTRACTEXPENSE:
          - AMOUNT
          - CONTRACTDETAILKEY
          - CONTRACTID
          - ITEMID
          - LOCATIONID
          - POSTINGDATE
          - TEMPLATENAME
        - CONTRACTEXPENSETEMPLATE:
          - DESCRIPTION
          - METHOD
          - NAME
          - POSTINGTYPE
        - CONTRACTITEMPRICELIST:
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
          - VARUNITDIVSR
        - CONTRACTMEABUNDLE:
          - ADJUSTMENTPROCESS
          - APPLYTOJOURNAL1
          - CONTRACTID
          - CONTRACTMEABUNDLEENTRIES.CONTRACTMEABUNDLEENTRY.BUNDLENO
          - CONTRACTMEABUNDLEENTRIES.CONTRACTMEABUNDLEENTRY.CONTRACTDETAILLINENO
          - DESCRIPTION
          - EFFECTIVEDATE
          - NAME
          - TYPE
        - CONTRACTPRICELIST:
          - NAME
        - CONTRACTREVENUETEMPLATE:
          - DESCRIPTION
          - METHOD
          - NAME
          - POSTINGTYPE
        - CONTRACTTYPE:
          - DESCRIPTION
          - NAME
          - PARENT.NAME
          - STATUS
        - CONTRACTUSAGE:
          - CONTRACTID
          - CONTRACTLINENO
          - QUANTITY
          - USAGEDATE
        - COSTTYPE:
          - ACTUALBEGINDATE
          - COSTUNITDESCRIPTION
          - DESCRIPTION
          - PROJECTID
          - STANDARDCOSTTYPEID
          - TASKID
        - CUSTOMER:
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
          - TERRITORYID
        - DEPARTMENT:
          - CUSTTITLE
          - DEPARTMENTID
          - PARENTID
          - STATUS
          - SUPERVISORID
          - TITLE
        - DUNNINGDEFINITION:
          - CURRENCY
          - DUNNINGDEFINITIONID
          - EMAILTEMPLATEKEY
          - MAXAMOUNT
          - MAXDAYS
          - MINAMOUNT
          - MINDAYS
          - NOTICESEQUENCE
          - PRINTTEMPLATENAME
        - EEACCOUNTLABEL:
          - ACCOUNTLABEL
          - DESCRIPTION
          - GLACCOUNTNO
          - OFFSETGLACCOUNTNO
          - STATUS
        - EMPLOYEE:
          - PERSONALINFO.CONTACTNAME
        - EMPLOYEEPOSITION:
          - DESCRIPTION
          - NAME
          - POSITIONID
        - EXCHANGERATE:
          - EXCHANGERATEENTRIES.EXCHANGERATEENTRY.EFFECTIVE_START_DATE
          - EXCHANGERATEENTRIES.EXCHANGERATEENTRY.EXCHANGE_RATE
          - EXCHANGERATEENTRIES.EXCHANGERATEENTRY.RECIPROCAL_RATE
          - FROM_CURRENCY
          - TO_CURRENCY
          - TYPENAME
        - GCBOOK:
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
          - SOURCEBOOKID
        - GCBOOKACCTRATETYPE:
          - BOOKID
          - GLACCOUNTNO
          - GLACCTRATETYPES
          - OVERRIDERATE
        - GCBOOKADJJOURNAL:
          - BOOKID
          - BOOKTYPE
          - SYMBOL
          - TITLE
        - GCBOOKELIMACCOUNT:
          - BOOKID
          - GLACCOUNTNO
        - GCBOOKENTITY:
          - BOOKID
          - LOCATIONID
        - GCOWNERSHIPSTRUCTURE:
          - AUTOELIMINATION
          - DESCRIPTION
          - SOURCEBOOKID
          - STATUS
          - STRUCTURENAME
        - GCOWNERSHIPSTRUCTUREDETAIL:
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
          - STRUCTURENAME
        - GENINVOICEPOLICY:
          - CONTRACTID
          - INCLUDECONTRACTS
          - INCLUDECONTRACTUSAGE
          - NAME
        - GENINVOICEPREVIEW:
          - ASOFDATE
          - DOCPARID
          - GLPOSTDATE
          - INCLUDECONTRACTS
          - INCLUDECONTRACTUSAGE
          - INVOICEBY
          - INVOICEDATE
        - GENINVOICERUN:
          - PREVIEWKEY
        - GLACCOUNT:
          - ACCOUNTNO
          - TITLE
        - GLACCTALLOCATION:
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
          - METHODOLOGY
        - GLACCTALLOCATIONGRP:
          - DESCRIPTION
          - GLACCTALLOCATIONGRPMEMBERS.GLACCTALLOCATIONGRPMEMBER.GLACCTALLOCATIONID
          - GRPERRORPROCESSINGMETHOD
          - NAME
        - GLACCTALLOCATIONRUN:
          - ASOFDATE
          - EMAIL
          - GLACCTALLOCATION
          - GLPOSTINGDATE
        - GLACCTGRP:
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
          - VENDORID
        - GLACCTGRPPURPOSE:
          - NAME
        - GLBATCH:
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
          - REVERSEDATE
        - GLBUDGETHEADER:
          - BUDGETID
          - DEFAULT_BUDGET
          - DESCRIPTION
          - GLBUDGETITEMS.GLBUDGETITEM.ACCT_NO
          - GLBUDGETITEMS.GLBUDGETITEM.AMOUNT
          - GLBUDGETITEMS.GLBUDGETITEM.DEPT_NO
          - GLBUDGETITEMS.GLBUDGETITEM.LOCATION_NO
          - GLBUDGETITEMS.GLBUDGETITEM.PERIODNAME
        - ICCYCLECOUNT:
          - CYCLECOUNTDESC
          - EMPUSERID
          - SHOWQTYONHAND
          - WAREHOUSEID
        - ICCYCLECOUNTENTRY:
          - CYCLECOUNTKEY
          - ITEMID
        - ICTRANSFER:
          - DESCRIPTION
          - ICTRANSFERITEMS.ICTRANSFERITEM.IN_OUT
          - ICTRANSFERITEMS.ICTRANSFERITEM.ITEMID
          - ICTRANSFERITEMS.ICTRANSFERITEM.LOCATIONID
          - ICTRANSFERITEMS.ICTRANSFERITEM.QUANTITY
          - ICTRANSFERITEMS.ICTRANSFERITEM.UNIT
          - ICTRANSFERITEMS.ICTRANSFERITEM.WAREHOUSEID
          - TRANSACTIONDATE
          - TRANSFERTYPE
        - ITEM:
          - ITEMID
          - ITEMTYPE
          - NAME
        - ITEMCROSSREF:
          - ITEMALIASDESC
          - ITEMALIASID
          - ITEMID
          - REFTYPE
          - VENDORID
        - LABORCLASS:
          - DESCRIPTION
          - LABORCLASSID
          - NAME
        - LABORSHIFT:
          - DESCRIPTION
          - LABORSHIFTID
          - NAME
        - LABORUNION:
          - DESCRIPTION
          - LABORUNIONID
          - NAME
        - LOCATION:
          - CONTACTINFO.CONTACTNAME
          - CUSTTITLE
          - ENDDATE
          - LOCATIONID
          - NAME
          - PARENTID
          - SHIPTO.CONTACTNAME
          - STARTDATE
          - STATUS
          - SUPERVISORID
        - OBSPCTCOMPLETED:
          - ASOFDATE
          - NOTE
          - PERCENT
          - PROJECTKEY
          - TASKKEY
          - TYPE
        - PAYROLLREPORTCHECK:
          - CHECKID
          - CHECKSTATUS
          - CHECKTYPE
          - EMPLOYEEID
          - EXTERNALENTITYID
          - LEGALENTITYID
          - PAYPERIODNUMBER
          - PAYROLLYEAR
          - REVISIONNUMBER
        - PAYROLLREPORTEMPLOYEE:
          - EFFECTIVEDATE
          - EMPLOYEEID
          - PAYGROUPID
        - PAYROLLREPORTGROSSPAY:
          - CHECKID
          - EMPLOYEEID
          - GROSSPAY
          - GROSSPAYID
          - ISPREMIUM
          - TIMECARDID
        - PAYROLLREPORTPAYMODIFIER:
          - CHECKID
          - EMPLOYEEID
          - PAYMODIFIERCATEGORY
          - PAYMODIFIERID
          - PAYMODIFIERTYPE
          - PRETAXCATCHUPCONTRIBUTIONAMT
          - PRETAXCONTRIBUTIONAMT
          - TIMECARDID
        - PAYROLLREPORTPTOACCRUALSCHEDULE:
          - EFFECTIVEDATE
          - PAYROLLREPORTPTOACCRUALSCHEDULELINES.PAYROLLREPORTPTOACCRUALSCHEDULELINE.MINIMUMYEARSOFSERVICE
          - PAYROLLREPORTPTOACCRUALSCHEDULELINES.PAYROLLREPORTPTOACCRUALSCHEDULELINE.PAYROLLREPORTPTOACCRUALSCHEDULERATES.PAYROLLREPORTPTOACCRUALSCHEDULERATE.WORKEDHOURSID
          - PTOACCRUALSCHEDULEID
          - PTOTYPEID
        - PAYROLLREPORTPTOACTIVITY:
          - ACCRUALSCHEDULEID
          - CHECKID
          - DEDUCTIONTAKEN
          - EMPLOYEEID
          - HOURS
          - PTOACTIVITYID
          - SOURCE
          - TIMECARDID
          - WORKEDHOURSID
        - PAYROLLREPORTTAX:
          - CHECKID
          - EMPLOYEEID
          - EMPLOYEETAXAMOUNT
          - EMPLOYERTAXAMOUNT
          - TAXCATEGORYID
          - TAXID
          - TIMECARDID
        - PAYROLLREPORTTAXSETUP:
          - REPORTAS
          - REPORTINGLEVEL
          - STATE
          - TAXCATEGORYID
          - TAXID
          - TAXTYPE
        - PAYROLLREPORTTIMECARD:
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
          - WORKUNIONID
        - PAYROLLREPORTTRADE:
          - PAYROLLREPORTTRADELEVEL.CLASSLEVEL
          - PAYROLLREPORTTRADELEVEL.CLASSPERSCENT
          - PAYROLLREPORTTRADELEVEL.TRADEKEY
          - PAYROLLREPORTTRADELEVEL.TRADELEVELID
          - REVISIONNUMBER
          - TRADEID
          - WORKCLASSIFICATION
          - WORKCLASSIFICATIONCODE
        - PJESTIMATE:
          - ENTRIES.PJESTIMATEENTRY.AMOUNT
          - ENTRIES.PJESTIMATEENTRY.MEMO
          - ENTRIES.PJESTIMATEENTRY.WFTYPE
          - PJESTIMATEID
          - PROJECTID
        - PJESTIMATEENTRY:
          - EUOM
          - PJESTIMATEID
          - QTY
          - UNITCOST
          - WFTYPE
        - PJESTIMATETYPE:
          - NAME
          - SELECTEDWFTYPES
        - PODOCUMENTPARAMS:
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
          - UPDATES_GL
        - PROJECT:
          - NAME
          - PROJECTCATEGORY
        - PROJECTCHANGEORDER:
          - CHANGEREQUESTSTATUSNAME
          - ITEMID
          - PROJECTCHANGEORDERDATE
          - PROJECTCHANGEORDERID
          - PROJECTID
        - PROJECTCONTRACT:
          - CONTRACTDATE
          - CUSTOMERID
          - NAME
          - PROJECTCONTRACTID
          - PROJECTID
        - PROJECTCONTRACTLINE:
          - ACCOUNTNO
          - BILLINGTYPE
          - CONTRACTLINEDATE
          - ITEMID
          - MAXIMUMBILLING
          - NAME
          - PROJECTCONTRACTID
          - PROJECTCONTRACTLINEID
          - PROJECTID
        - PROJECTCONTRACTTYPE:
          - PROJECTCONTRACTTYPEID
          - PROJECTCONTRACTTYPENAME
        - PROVIDERBANKACCOUNT:
          - PROVIDERID
          - VENDORID
        - PROVIDERVENDOR:
          - PROVIDERID
          - STATUS
          - VENDORID
        - RATETABLE:
          - RATETABLEID
        - RECURGLACCTALLOCATION:
          - EMAIL
          - ENDINGON
          - GLACCTALLOCATION
          - ISPERIODEND
          - PLANNAME
          - REPEATBY
          - REPEATINTERVAL
          - STARTDATE
        - REPORTINGPERIOD:
          - BUDGETING
          - END_DATE
          - HEADER1
          - HEADER2
          - NAME
          - START_DATE
          - STATUS
        - STANDARDCOSTTYPE:
          - COSTUNITDESCRIPTION
          - DESCRIPTION
          - NAME
          - STANDARDCOSTTYPEID
        - STANDARDTASK:
          - COSTUNITDESCRIPTION
          - DESCRIPTION
          - NAME
          - STANDARDTASKID
          - STANDARDTASKSTANDARDCOSTTYPES.STANDARDTASKSTANDARDCOSTTYPE.STANDARDCOSTTYPEID
          - TASKNO
          - TIMETYPENAME
        - STATACCOUNT:
          - ACCOUNTNO
          - TITLE
        - TASK:
          - NAME
          - PROJECTID
          - TASKID
          - TASKSTATUS
        - TIMESHEET:
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
          - TIMESHEETENTRIES.TIMESHEETENTRY.VENDORID
        - USERINFO:
          - ADMIN
          - CONTACTINFO.EMAIL1
          - CONTACTINFO.FIRSTNAME
          - CONTACTINFO.LASTNAME
          - DESCRIPTION
          - LOGINID
          - SSO_ENABLED
          - SSO_FEDERATED_ID
          - STATUS
          - USERTYPE
        - USERROLES:
          - ROLENAME
          - USERID
        - VENDOR:
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
          - VENDTYPE
        - WAREHOUSE:
          - LOC.LOCATIONID
          - NAME
          - WAREHOUSEID
        - ZONE:
          - ZONEDESC
          - ZONEID"""
        return self.execute("create", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_achbankconfiguration(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_achbankconfiguration".
        
        Fields (from Docs samples):
        - achbankid
        - destinationid
        - destinationname
        - eofmarker
        - originid
        - originname
        - referencecode
        - status"""
        return self.execute("create_achbankconfiguration", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_apaccountlabel(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_apaccountlabel".
        
        Fields (from Docs samples):
        - accountlabel
        - description
        - glaccountno
        - offsetglaccountno
        - status"""
        return self.execute("create_apaccountlabel", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_apadjustment(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_apadjustment".
        
        Fields (from Docs samples):
        - action
        - adjustmentno
        - apadjustmentitems.lineitem.amount
        - apadjustmentitems.lineitem.classid
        - apadjustmentitems.lineitem.customerid
        - apadjustmentitems.lineitem.customfields.customfield.customfieldname
        - apadjustmentitems.lineitem.customfields.customfield.customfieldvalue
        - apadjustmentitems.lineitem.departmentid
        - apadjustmentitems.lineitem.employeeid
        - apadjustmentitems.lineitem.glaccountno
        - apadjustmentitems.lineitem.itemid
        - apadjustmentitems.lineitem.key
        - apadjustmentitems.lineitem.locationid
        - apadjustmentitems.lineitem.memo
        - apadjustmentitems.lineitem.offsetglaccountno
        - apadjustmentitems.lineitem.projectid
        - apadjustmentitems.lineitem.vendorid
        - apadjustmentitems.lineitem.warehouseid
        - basecurr
        - batchkey
        - billno
        - currency
        - customfields.customfield.customfieldname
        - customfields.customfield.customfieldvalue
        - datecreated.day
        - datecreated.month
        - datecreated.year
        - dateposted.day
        - dateposted.month
        - dateposted.year
        - description
        - exchratedate.day
        - exchratedate.month
        - exchratedate.year
        - exchratetype
        - externalid
        - nogl
        - vendorid"""
        return self.execute("create_apadjustment", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_apadjustmentbatch(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_apadjustmentbatch".
        
        Fields (from Docs samples):
        - batchtitle
        - datecreated.day
        - datecreated.month
        - datecreated.year"""
        return self.execute("create_apadjustmentbatch", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_appayment(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_appayment".
        
        Fields (from Docs samples):
        - bankaccountid
        - billno
        - checkdate.day
        - checkdate.month
        - checkdate.year
        - checkno
        - memo
        - payitems.payitem.departmentid
        - payitems.payitem.glaccountno
        - payitems.payitem.item1099
        - payitems.payitem.locationid
        - payitems.payitem.paymentamount
        - vendorid"""
        return self.execute("create_appayment", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_apterm(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_apterm".
        
        Fields (from Docs samples):
        - description
        - disccalcon
        - discount.discamount
        - discount.discday
        - discount.discfrom
        - discount.discgracedays
        - discount.discpercamn
        - due.dueday
        - due.duefrom
        - name
        - penalty.pen_type
        - penalty.penamount
        - penalty.pengracedays
        - penalty.penpercamn"""
        return self.execute("create_apterm", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_araccountlabel(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_araccountlabel".
        
        Fields (from Docs samples):
        - accountlabel
        - description
        - glaccountno
        - offsetglaccountno
        - status"""
        return self.execute("create_araccountlabel", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_aradjustment(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_aradjustment".
        
        Fields (from Docs samples):
        - adjustmentno
        - aradjustmentitems.lineitem.amount
        - aradjustmentitems.lineitem.classid
        - aradjustmentitems.lineitem.customerid
        - aradjustmentitems.lineitem.departmentid
        - aradjustmentitems.lineitem.employeeid
        - aradjustmentitems.lineitem.glaccountno
        - aradjustmentitems.lineitem.itemid
        - aradjustmentitems.lineitem.locationid
        - aradjustmentitems.lineitem.memo
        - aradjustmentitems.lineitem.projectid
        - aradjustmentitems.lineitem.vendorid
        - customerid
        - datecreated.day
        - datecreated.month
        - datecreated.year
        - description
        - invoiceno"""
        return self.execute("create_aradjustment", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_aradjustmentbatch(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_aradjustmentbatch".
        
        Fields (from Docs samples):
        - batchtitle
        - datecreated.day
        - datecreated.month
        - datecreated.year"""
        return self.execute("create_aradjustmentbatch", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_arpayment(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_arpayment".
        
        Fields (from Docs samples):
        - arpaymentitem.amount
        - arpaymentitem.invoicekey
        - bankaccountid
        - basecurr
        - currency
        - customerid
        - datereceived.day
        - datereceived.month
        - datereceived.year
        - exchratetype
        - overpaydeptid
        - overpaylocid
        - paymentamount
        - paymentmethod
        - refid
        - translatedamount"""
        return self.execute("create_arpayment", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_arpaymentbatch(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_arpaymentbatch".
        
        Fields (from Docs samples):
        - bankaccountid
        - batchtitle
        - datecreated.day
        - datecreated.month
        - datecreated.year"""
        return self.execute("create_arpaymentbatch", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_arterm(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_arterm".
        
        Fields (from Docs samples):
        - description
        - disccalcon
        - discount.discamount
        - discount.discday
        - discount.discfrom
        - discount.discgracedays
        - discount.discpercamn
        - due.dueday
        - due.duefrom
        - name
        - penalty.pen_type
        - penalty.penamount
        - penalty.pengracedays
        - penalty.penpercamn"""
        return self.execute("create_arterm", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_bill(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_bill".
        
        Fields (from Docs samples):
        - action
        - basecurr
        - batchkey
        - billitems.lineitem.amount
        - billitems.lineitem.billable
        - billitems.lineitem.classid
        - billitems.lineitem.contractid
        - billitems.lineitem.customerid
        - billitems.lineitem.customfields.customfield.customfieldname
        - billitems.lineitem.customfields.customfield.customfieldvalue
        - billitems.lineitem.departmentid
        - billitems.lineitem.employeeid
        - billitems.lineitem.glaccountno
        - billitems.lineitem.item1099
        - billitems.lineitem.itemid
        - billitems.lineitem.key
        - billitems.lineitem.locationid
        - billitems.lineitem.memo
        - billitems.lineitem.offsetglaccountno
        - billitems.lineitem.projectid
        - billitems.lineitem.totaldue
        - billitems.lineitem.totalpaid
        - billitems.lineitem.vendorid
        - billitems.lineitem.warehouseid
        - billno
        - currency
        - customfields.customfield.customfieldname
        - customfields.customfield.customfieldvalue
        - datecreated.day
        - datecreated.month
        - datecreated.year
        - datedue.day
        - datedue.month
        - datedue.year
        - dateposted.day
        - dateposted.month
        - dateposted.year
        - description
        - exchratedate.day
        - exchratedate.month
        - exchratedate.year
        - exchratetype
        - externalid
        - nogl
        - onhold
        - payto.contactname
        - ponumber
        - returnto.contactname
        - supdocid
        - termname
        - vendorid"""
        return self.execute("create_bill", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_billbatch(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_billbatch".
        
        Fields (from Docs samples):
        - batchtitle
        - datecreated.day
        - datecreated.month
        - datecreated.year"""
        return self.execute("create_billbatch", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_class(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_class".
        
        Fields (from Docs samples):
        - classid
        - name"""
        return self.execute("create_class", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_consolidation(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_consolidation".
        
        Fields (from Docs samples):
        - bookid
        - changesonly
        - email
        - entities.csnentity.bsrate
        - entities.csnentity.entityid
        - entities.csnentity.warate
        - offline
        - reportingperiodname
        - updatesucceedingperiods"""
        return self.execute("create_consolidation", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_contact(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_contact".
        
        Fields (from Docs samples):
        - contactname
        - printas"""
        return self.execute("create_contact", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_contacttaxgroup(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_contacttaxgroup".
        
        Fields (from Docs samples):
        - name"""
        return self.execute("create_contacttaxgroup", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_customer(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_customer".
        
        Fields (from Docs samples):
        - contactinfo.contact.contactname
        - contactinfo.contact.printas
        - customerid
        - name
        - primary.contactname"""
        return self.execute("create_customer", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_customerbankaccount(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_customerbankaccount".
        
        Fields (from Docs samples):
        - accountholder
        - accountnumber
        - accounttype
        - bankname
        - customerid
        - routingnumber"""
        return self.execute("create_customerbankaccount", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_customerchargecard(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_customerchargecard".
        
        Fields (from Docs samples):
        - cardnum
        - cardtype
        - customerid
        - exp_month
        - exp_year
        - mailaddress.address1
        - mailaddress.address2
        - mailaddress.city
        - mailaddress.country
        - mailaddress.state
        - mailaddress.zip"""
        return self.execute("create_customerchargecard", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_department(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_department".
        
        Fields (from Docs samples):
        - departmentid
        - title"""
        return self.execute("create_department", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_earningtype(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_earningtype".
        
        Fields (from Docs samples):
        - billableacctno
        - method
        - name
        - nonbillableacctno
        - ratemultiplier"""
        return self.execute("create_earningtype", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_employee(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_employee".
        
        Fields (from Docs samples):
        - employeeid
        - locationid
        - personalinfo.contactname
        - title"""
        return self.execute("create_employee", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_employeerate(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_employeerate".
        
        Fields (from Docs samples):
        - billingrate
        - employeeid
        - ratestartdate.day
        - ratestartdate.month
        - ratestartdate.year
        - salaryrate"""
        return self.execute("create_employeerate", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_expenseadjustmentreport(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_expenseadjustmentreport".
        
        Fields (from Docs samples):
        - adjustmentno
        - basecurr
        - currency
        - datecreated.day
        - datecreated.month
        - datecreated.year
        - dateposted.day
        - dateposted.month
        - dateposted.year
        - description
        - docnumber
        - employeeid
        - expenseadjustments.expenseadjustment.amount
        - expenseadjustments.expenseadjustment.billable
        - expenseadjustments.expenseadjustment.classid
        - expenseadjustments.expenseadjustment.currency
        - expenseadjustments.expenseadjustment.customerid
        - expenseadjustments.expenseadjustment.departmentid
        - expenseadjustments.expenseadjustment.employeeid
        - expenseadjustments.expenseadjustment.exchratedate.day
        - expenseadjustments.expenseadjustment.exchratedate.month
        - expenseadjustments.expenseadjustment.exchratedate.year
        - expenseadjustments.expenseadjustment.exchratetype
        - expenseadjustments.expenseadjustment.expensedate.day
        - expenseadjustments.expenseadjustment.expensedate.month
        - expenseadjustments.expenseadjustment.expensedate.year
        - expenseadjustments.expenseadjustment.expensetype
        - expenseadjustments.expenseadjustment.exppmttype
        - expenseadjustments.expenseadjustment.itemid
        - expenseadjustments.expenseadjustment.locationid
        - expenseadjustments.expenseadjustment.memo
        - expenseadjustments.expenseadjustment.projectid
        - expenseadjustments.expenseadjustment.quantity
        - expenseadjustments.expenseadjustment.rate
        - expenseadjustments.expenseadjustment.trx_amount
        - expenseadjustments.expenseadjustment.vendorid
        - supdocid"""
        return self.execute("create_expenseadjustmentreport", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_expensepaymenttype(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_expensepaymenttype".
        
        Fields (from Docs samples):
        - description
        - name
        - nonreimbursable
        - offsetacctno"""
        return self.execute("create_expensepaymenttype", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_expensereport(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_expensereport".
        
        Fields (from Docs samples):
        - datecreated.day
        - datecreated.month
        - datecreated.year
        - description
        - employeeid
        - expenses.expense.amount
        - expenses.expense.billable
        - expenses.expense.departmentid
        - expenses.expense.employeeid
        - expenses.expense.expensedate.day
        - expenses.expense.expensedate.month
        - expenses.expense.expensedate.year
        - expenses.expense.expensetype
        - expenses.expense.locationid
        - expenses.expense.memo
        - expenses.expense.paidfor
        - expenses.expense.projectid
        - state"""
        return self.execute("create_expensereport", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_expensereportbatch(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_expensereportbatch".
        
        Fields (from Docs samples):
        - batchtitle
        - datecreated.day
        - datecreated.month
        - datecreated.year"""
        return self.execute("create_expensereportbatch", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_expensetype(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_expensetype".
        
        Fields (from Docs samples):
        - description
        - expensetype
        - glaccountno
        - offsetglaccountno
        - status"""
        return self.execute("create_expensetype", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_glaccount(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_glaccount".
        
        Fields (from Docs samples):
        - glaccountno
        - title"""
        return self.execute("create_glaccount", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_gltransaction(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_gltransaction".
        
        Fields (from Docs samples):
        - datecreated.day
        - datecreated.month
        - datecreated.year
        - description
        - gltransactionentries.glentry.amount
        - gltransactionentries.glentry.currency
        - gltransactionentries.glentry.departmentid
        - gltransactionentries.glentry.exchratetype
        - gltransactionentries.glentry.glaccountno
        - gltransactionentries.glentry.locationid
        - gltransactionentries.glentry.memo
        - gltransactionentries.glentry.trtype
        - journalid
        - reversedate.day
        - reversedate.month
        - reversedate.year"""
        return self.execute("create_gltransaction", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_ictransaction(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_ictransaction".
        
        Fields (from Docs samples):
        - basecurr
        - createdfrom
        - datecreated.day
        - datecreated.month
        - datecreated.year
        - documentno
        - ictransitems.ictransitem.classid
        - ictransitems.ictransitem.contractid
        - ictransitems.ictransitem.cost
        - ictransitems.ictransitem.customerid
        - ictransitems.ictransitem.departmentid
        - ictransitems.ictransitem.employeeid
        - ictransitems.ictransitem.itemdesc
        - ictransitems.ictransitem.itemid
        - ictransitems.ictransitem.locationid
        - ictransitems.ictransitem.projectid
        - ictransitems.ictransitem.quantity
        - ictransitems.ictransitem.unit
        - ictransitems.ictransitem.vendorid
        - ictransitems.ictransitem.warehouseid
        - message
        - referenceno
        - state
        - transactiontype"""
        return self.execute("create_ictransaction", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_invoice(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_invoice".
        
        Fields (from Docs samples):
        - action
        - basecurr
        - batchkey
        - billto.contactname
        - currency
        - customerid
        - customfields.customfield.customfieldname
        - customfields.customfield.customfieldvalue
        - datecreated.day
        - datecreated.month
        - datecreated.year
        - datedue.day
        - datedue.month
        - datedue.year
        - dateposted.day
        - dateposted.month
        - dateposted.year
        - description
        - exchratedate.day
        - exchratedate.month
        - exchratedate.year
        - exchratetype
        - externalid
        - invoiceitems.lineitem.accountlabel
        - invoiceitems.lineitem.amount
        - invoiceitems.lineitem.classid
        - invoiceitems.lineitem.customerid
        - invoiceitems.lineitem.customfields.customfield.customfieldname
        - invoiceitems.lineitem.customfields.customfield.customfieldvalue
        - invoiceitems.lineitem.defrevaccount
        - invoiceitems.lineitem.departmentid
        - invoiceitems.lineitem.employeeid
        - invoiceitems.lineitem.itemid
        - invoiceitems.lineitem.key
        - invoiceitems.lineitem.locationid
        - invoiceitems.lineitem.memo
        - invoiceitems.lineitem.offsetglaccountno
        - invoiceitems.lineitem.projectid
        - invoiceitems.lineitem.revrecenddate.day
        - invoiceitems.lineitem.revrecenddate.month
        - invoiceitems.lineitem.revrecenddate.year
        - invoiceitems.lineitem.revrecstartdate.day
        - invoiceitems.lineitem.revrecstartdate.month
        - invoiceitems.lineitem.revrecstartdate.year
        - invoiceitems.lineitem.revrectemplate
        - invoiceitems.lineitem.totaldue
        - invoiceitems.lineitem.totalpaid
        - invoiceitems.lineitem.vendorid
        - invoiceitems.lineitem.warehouseid
        - invoiceno
        - nogl
        - ponumber
        - shipto.contactname
        - supdocid
        - termname"""
        return self.execute("create_invoice", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_invoicebatch(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_invoicebatch".
        
        Fields (from Docs samples):
        - batchtitle
        - datecreated.day
        - datecreated.month
        - datecreated.year"""
        return self.execute("create_invoicebatch", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_item(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_item".
        
        Fields (from Docs samples):
        - itemid
        - itemtype
        - name"""
        return self.execute("create_item", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_itemtaxgroup(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_itemtaxgroup".
        
        Fields (from Docs samples):
        - name"""
        return self.execute("create_itemtaxgroup", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_location(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_location".
        
        Fields (from Docs samples):
        - locationid
        - name"""
        return self.execute("create_location", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_paymentrequest(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_paymentrequest".
        
        Fields (from Docs samples):
        - bankaccountid
        - documentnumber
        - grouppayments
        - memo
        - paymentcontact
        - paymentdate.day
        - paymentdate.month
        - paymentdate.year
        - paymentdescription
        - paymentmethod
        - paymentoption
        - paymentrequestitems.paymentrequestitem.credittoapply
        - paymentrequestitems.paymentrequestitem.discounttoapply
        - paymentrequestitems.paymentrequestitem.key
        - paymentrequestitems.paymentrequestitem.paymentamount
        - vendorid"""
        return self.execute("create_paymentrequest", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_popricelist(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_popricelist".
        
        Fields (from Docs samples):
        - name"""
        return self.execute("create_popricelist", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_potransaction(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_potransaction".
        
        Fields (from Docs samples):
        - customfields
        - datecreated.day
        - datecreated.month
        - datecreated.year
        - datedue.day
        - datedue.month
        - datedue.year
        - exchratetype
        - payto.contactname
        - potransitems.potransitem.departmentid
        - potransitems.potransitem.itemid
        - potransitems.potransitem.locationid
        - potransitems.potransitem.price
        - potransitems.potransitem.quantity
        - potransitems.potransitem.unit
        - referenceno
        - transactiontype
        - vendordocno
        - vendorid"""
        return self.execute("create_potransaction", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_recurringbill(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_recurringbill".
        
        Fields (from Docs samples):
        - datecreated.day
        - datecreated.month
        - datecreated.year
        - description
        - docnumber
        - ending.occur
        - eom
        - interval
        - modenew
        - recordid
        - recurbillitems.recurlineitem.amount
        - recurbillitems.recurlineitem.departmentid
        - recurbillitems.recurlineitem.glaccountno
        - recurbillitems.recurlineitem.locationid
        - startdate.day
        - startdate.month
        - startdate.year
        - termname
        - vendorid"""
        return self.execute("create_recurringbill", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_recurringinvoice(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_recurringinvoice".
        
        Fields (from Docs samples):
        - customerid
        - datecreated.day
        - datecreated.month
        - datecreated.year
        - description
        - docnumber
        - ending.occur
        - eom
        - interval
        - modenew
        - recordid
        - recurinvoiceitems.recurlineitem.amount
        - recurinvoiceitems.recurlineitem.departmentid
        - recurinvoiceitems.recurlineitem.glaccountno
        - recurinvoiceitems.recurlineitem.locationid
        - startdate.day
        - startdate.month
        - startdate.year
        - termname"""
        return self.execute("create_recurringinvoice", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_recursotransaction(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_recursotransaction".
        
        Fields (from Docs samples):
        - accounttype
        - creditcardtype
        - customerid
        - ending.occur
        - eom
        - glaccountkey
        - interval
        - message
        - modenew
        - payinfull
        - paymethod
        - recursotransitems.recursotransitem.itemid
        - recursotransitems.recursotransitem.locationid
        - recursotransitems.recursotransitem.price
        - recursotransitems.recursotransitem.quantity
        - referenceno
        - shippingmethod
        - startdate.day
        - startdate.month
        - startdate.year
        - termname
        - transactiontype"""
        return self.execute("create_recursotransaction", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_reimbursementrequest(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_reimbursementrequest".
        
        Fields (from Docs samples):
        - bankaccountid
        - documentnumber
        - employeeid
        - eppaymentrequestitems.eppaymentrequestitem.credittoapply
        - eppaymentrequestitems.eppaymentrequestitem.key
        - eppaymentrequestitems.eppaymentrequestitem.paymentamount
        - memo
        - paymentcontact
        - paymentdate.day
        - paymentdate.month
        - paymentdate.year
        - paymentdescription
        - paymentmethod
        - paymentoption"""
        return self.execute("create_reimbursementrequest", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_savingsaccount(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_savingsaccount".
        
        Fields (from Docs samples):
        - bankaccountid
        - bankaccountno
        - bankname
        - currency"""
        return self.execute("create_savingsaccount", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_sopricelist(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_sopricelist".
        
        Fields (from Docs samples):
        - name"""
        return self.execute("create_sopricelist", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_sotransaction(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_sotransaction".
        
        Fields (from Docs samples):
        - basecurr
        - billto.contactname
        - createdfrom
        - currency
        - customerid
        - customfields
        - datecreated.day
        - datecreated.month
        - datecreated.year
        - datedue.day
        - datedue.month
        - datedue.year
        - documentno
        - exchratetype
        - message
        - origdocdate.day
        - origdocdate.month
        - origdocdate.year
        - referenceno
        - shippingmethod
        - shipto.contactname
        - sotransitems.sotransitem.bundlenumber
        - sotransitems.sotransitem.departmentid
        - sotransitems.sotransitem.discsurchargememo
        - sotransitems.sotransitem.itemid
        - sotransitems.sotransitem.locationid
        - sotransitems.sotransitem.price
        - sotransitems.sotransitem.quantity
        - sotransitems.sotransitem.unit
        - state
        - subtotals.subtotal.departmentid
        - subtotals.subtotal.description
        - subtotals.subtotal.locationid
        - subtotals.subtotal.total
        - termname
        - transactiontype"""
        return self.execute("create_sotransaction", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_statglaccount(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_statglaccount".
        
        Fields (from Docs samples):
        - glaccountno
        - title"""
        return self.execute("create_statglaccount", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_statgltransaction(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_statgltransaction".
        
        Fields (from Docs samples):
        - datecreated.day
        - datecreated.month
        - datecreated.year
        - description
        - journalid
        - statgltransactionentries.glentry.amount
        - statgltransactionentries.glentry.departmentid
        - statgltransactionentries.glentry.glaccountno
        - statgltransactionentries.glentry.locationid
        - statgltransactionentries.glentry.memo
        - statgltransactionentries.glentry.trtype"""
        return self.execute("create_statgltransaction", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_stkittransaction(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_stkittransaction".
        
        Fields (from Docs samples):
        - createdfrom
        - datecreated.day
        - datecreated.month
        - datecreated.year
        - documentno
        - message
        - stkittransitems.stkittransitem.itemdesc
        - stkittransitems.stkittransitem.itemdetails.itemdetail.bin
        - stkittransitems.stkittransitem.itemdetails.itemdetail.componentid
        - stkittransitems.stkittransitem.itemdetails.itemdetail.itemexpiration.day
        - stkittransitems.stkittransitem.itemdetails.itemdetail.itemexpiration.month
        - stkittransitems.stkittransitem.itemdetails.itemdetail.itemexpiration.year
        - stkittransitems.stkittransitem.itemdetails.itemdetail.lotno
        - stkittransitems.stkittransitem.itemdetails.itemdetail.quantity
        - stkittransitems.stkittransitem.itemid
        - stkittransitems.stkittransitem.quantity
        - stkittransitems.stkittransitem.unit
        - stkittransitems.stkittransitem.warehouseid
        - transactiontype"""
        return self.execute("create_stkittransaction", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_supdoc(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_supdoc".
        
        Fields (from Docs samples):
        - attachments.attachment.attachmentdata
        - attachments.attachment.attachmentname
        - attachments.attachment.attachmenttype
        - supdocdescription
        - supdocfoldername
        - supdocid"""
        return self.execute("create_supdoc", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_supdocfolder(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_supdocfolder".
        
        Fields (from Docs samples):
        - supdocfolderdescription
        - supdocfoldername
        - supdocparentfoldername"""
        return self.execute("create_supdocfolder", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_task(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_task".
        
        Fields (from Docs samples):
        - projectid
        - taskname"""
        return self.execute("create_task", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_territory(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_territory".
        
        Fields (from Docs samples):
        - managerid
        - name
        - parentid
        - status
        - territoryid"""
        return self.execute("create_territory", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_timesheet(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_timesheet".
        
        Fields (from Docs samples):
        - begindate.day
        - begindate.month
        - begindate.year
        - employeeid
        - timesheetdescription
        - timesheetitems.timesheetitem.customerid
        - timesheetitems.timesheetitem.customfields.customfield.customfieldname
        - timesheetitems.timesheetitem.customfields.customfield.customfieldvalue
        - timesheetitems.timesheetitem.departmentid
        - timesheetitems.timesheetitem.entrydate.day
        - timesheetitems.timesheetitem.entrydate.month
        - timesheetitems.timesheetitem.entrydate.year
        - timesheetitems.timesheetitem.itemid
        - timesheetitems.timesheetitem.locationid
        - timesheetitems.timesheetitem.qty"""
        return self.execute("create_timesheet", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_timetype(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_timetype".
        
        Fields (from Docs samples):
        - name"""
        return self.execute("create_timetype", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_vendor(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_vendor".
        
        Fields (from Docs samples):
        - contactinfo.contact.contactname
        - contactinfo.contact.printas
        - name
        - vendorid"""
        return self.execute("create_vendor", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def create_vendorentityaccountno(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "create_vendorentityaccountno".
        
        Fields (from Docs samples):
        - accountno
        - locationid
        - vendorid"""
        return self.execute("create_vendorentityaccountno", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def decline(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "decline".
        
        Fields (from Docs samples):
        - PODOCUMENT.COMMENT
        - PODOCUMENT.DOCID
        - TIMESHEET.COMMENT
        - TIMESHEET.RECORDNO"""
        return self.execute("decline", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def decline_appaymentrequest(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "decline_appaymentrequest".
        
        Fields (from Docs samples):
        - appaymentkeys.appaymentkey"""
        return self.execute("decline_appaymentrequest", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def decline_vendor(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "declineVendor".
        
        Fields (from Docs samples):
        - recordno
        - reviewcomments"""
        return self.execute("declineVendor", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete".
        
        Fields (from Docs samples):
        - (no fields listed)"""
        return self.execute("delete", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_achbankconfiguration(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_achbankconfiguration".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - achbankid"""
        return self.execute("delete_achbankconfiguration", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_apaccountlabel(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_apaccountlabel".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - accountlabel"""
        return self.execute("delete_apaccountlabel", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_apadjustment(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_apadjustment".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - key"""
        return self.execute("delete_apadjustment", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_apterm(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_apterm".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - name"""
        return self.execute("delete_apterm", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_araccountlabel(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_araccountlabel".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - accountlabel"""
        return self.execute("delete_araccountlabel", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_aradjustment(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_aradjustment".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - key"""
        return self.execute("delete_aradjustment", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_arterm(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_arterm".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - name"""
        return self.execute("delete_arterm", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_bill(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_bill".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - key"""
        return self.execute("delete_bill", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_class(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_class".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - key"""
        return self.execute("delete_class", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_contact(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_contact".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - contactname"""
        return self.execute("delete_contact", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_contacttaxgroup(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_contacttaxgroup".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - name"""
        return self.execute("delete_contacttaxgroup", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_customer(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_customer".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - customerid"""
        return self.execute("delete_customer", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_customerbankaccount(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_customerbankaccount".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - recordno"""
        return self.execute("delete_customerbankaccount", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_customerchargecard(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_customerchargecard".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - recordno"""
        return self.execute("delete_customerchargecard", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_department(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_department".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - departmentid"""
        return self.execute("delete_department", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_earningtype(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_earningtype".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - key"""
        return self.execute("delete_earningtype", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_employee(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_employee".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - employeeid"""
        return self.execute("delete_employee", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_employeerate(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_employeerate".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - key"""
        return self.execute("delete_employeerate", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_expenseadjustmentreport(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_expenseadjustmentreport".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - key"""
        return self.execute("delete_expenseadjustmentreport", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_expensepaymenttype(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_expensepaymenttype".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - name"""
        return self.execute("delete_expensepaymenttype", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_expensereport(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_expensereport".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - key"""
        return self.execute("delete_expensereport", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_expensetype(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_expensetype".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - expensetype"""
        return self.execute("delete_expensetype", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_glaccount(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_glaccount".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - glaccountno"""
        return self.execute("delete_glaccount", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_gltransaction(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_gltransaction".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - key"""
        return self.execute("delete_gltransaction", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_ictransaction(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_ictransaction".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - key"""
        return self.execute("delete_ictransaction", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_invoice(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_invoice".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - key"""
        return self.execute("delete_invoice", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_item(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_item".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - itemid"""
        return self.execute("delete_item", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_itemtaxgroup(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_itemtaxgroup".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - name"""
        return self.execute("delete_itemtaxgroup", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_location(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_location".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - locationid"""
        return self.execute("delete_location", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_otherreceipt(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_otherreceipt".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - key"""
        return self.execute("delete_otherreceipt", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_paymentrequest(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_paymentrequest".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - key"""
        return self.execute("delete_paymentrequest", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_popricelist(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_popricelist".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - name"""
        return self.execute("delete_popricelist", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_potransaction(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_potransaction".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - key"""
        return self.execute("delete_potransaction", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_recurringbill(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_recurringbill".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - key"""
        return self.execute("delete_recurringbill", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_recurringinvoice(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_recurringinvoice".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - key"""
        return self.execute("delete_recurringinvoice", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_recursotransaction(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_recursotransaction".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - key"""
        return self.execute("delete_recursotransaction", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_savingsaccount(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_savingsaccount".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - bankaccountid"""
        return self.execute("delete_savingsaccount", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_sopricelist(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_sopricelist".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - name"""
        return self.execute("delete_sopricelist", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_sotransaction(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_sotransaction".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - key"""
        return self.execute("delete_sotransaction", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_statglaccount(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_statglaccount".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - glaccountno"""
        return self.execute("delete_statglaccount", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_supdoc(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_supdoc".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - key"""
        return self.execute("delete_supdoc", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_supdocfolder(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_supdocfolder".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - key"""
        return self.execute("delete_supdocfolder", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_task(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_task".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - key"""
        return self.execute("delete_task", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_territory(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_territory".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - territoryid"""
        return self.execute("delete_territory", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_timesheet(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_timesheet".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - key"""
        return self.execute("delete_timesheet", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_timetype(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_timetype".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - key"""
        return self.execute("delete_timetype", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def delete_vendor(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "delete_vendor".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - vendorid"""
        return self.execute("delete_vendor", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def deliver(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "deliver".
        
        Fields (from Docs samples):
        - CONTRACTDETAIL.DELIVERYDATE
        - CONTRACTDETAIL.RECORDNO"""
        return self.execute("deliver", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def get(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "get".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - key
        - object"""
        return self.execute("get", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def get_accountbalances(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "get_accountbalances".
        
        Fields (from Docs samples):
        - glaccountno
        - reportingperiodname
        - showzerobalances"""
        return self.execute("get_accountbalances", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def get_accountbalancesbydimensions(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "get_accountbalancesbydimensions".
        
        Fields (from Docs samples):
        - endaccountno
        - enddate.day
        - enddate.month
        - enddate.year
        - groupby
        - locationid
        - startaccountno
        - startdate.day
        - startdate.month
        - startdate.year"""
        return self.execute("get_accountbalancesbydimensions", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def get_apisession(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "getAPISession".
        
        Fields (from Docs samples):
        - (no fields listed)"""
        return self.execute("getAPISession", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def get_applications(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "get_applications".
        
        Fields (from Docs samples):
        - (no fields listed)"""
        return self.execute("get_applications", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def get_approval_history(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "getApprovalHistory".
        
        Fields (from Docs samples):
        - docid
        - module"""
        return self.execute("getApprovalHistory", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def get_araging(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "get_araging".
        
        Fields (from Docs samples):
        - agingperiods
        - customerid
        - showdetails"""
        return self.execute("get_araging", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def get_audit_trail(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "getAuditTrail".
        
        Fields (from Docs samples):
        - object
        - recordNo"""
        return self.execute("getAuditTrail", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def get_companyprefs(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "get_companyprefs".
        
        Fields (from Docs samples):
        - (no fields listed)
        
        Operation attributes:
        - application"""
        return self.execute("get_companyprefs", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def get_dds_ddl(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "getDdsDdl".
        
        Fields (from Docs samples):
        - object"""
        return self.execute("getDdsDdl", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def get_dds_objects(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "getDdsObjects".
        
        Fields (from Docs samples):
        - (no fields listed)"""
        return self.execute("getDdsObjects", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def get_dimension_autofill_details(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "getDimensionAutofillDetails".
        
        Fields (from Docs samples):
        - (no fields listed)"""
        return self.execute("getDimensionAutofillDetails", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def get_dimension_relationships(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "getDimensionRelationships".
        
        Fields (from Docs samples):
        - (no fields listed)"""
        return self.execute("getDimensionRelationships", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def get_dimension_restricted_data(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "getDimensionRestrictedData".
        
        Fields (from Docs samples):
        - DimensionValue.dimension
        - DimensionValue.value"""
        return self.execute("getDimensionRestrictedData", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def get_dimension_restrictions(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "getDimensionRestrictions".
        
        Fields (from Docs samples):
        - (no fields listed)"""
        return self.execute("getDimensionRestrictions", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def get_dimensions(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "getDimensions".
        
        Fields (from Docs samples):
        - (no fields listed)"""
        return self.execute("getDimensions", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def get_financial_setup(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "getFinancialSetup".
        
        Fields (from Docs samples):
        - (no fields listed)"""
        return self.execute("getFinancialSetup", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def get_list(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "get_list".
        
        Fields (from Docs samples):
        - filter.logical.expression.field
        - filter.logical.expression.operator
        - filter.logical.expression.value
        - sorts.sortfield
        
        Operation attributes:
        - maxitems
        - object
        - showprivate"""
        return self.execute("get_list", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def get_transactions_to_approve(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "getTransactionsToApprove".
        
        Fields (from Docs samples):
        - module"""
        return self.execute("getTransactionsToApprove", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def get_trialbalance(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "get_trialbalance".
        
        Fields (from Docs samples):
        - debitcreditbalance
        - reportingperiodname
        - showdeptdetail
        - showlocdetail
        - showzerobalances"""
        return self.execute("get_trialbalance", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def get_user_permissions(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "getUserPermissions".
        
        Fields (from Docs samples):
        - userId"""
        return self.execute("getUserPermissions", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def get_vendor_approval_history(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "getVendorApprovalHistory".
        
        Fields (from Docs samples):
        - recordno"""
        return self.execute("getVendorApprovalHistory", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def get_vendors_to_approve(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "getVendorsToApprove".
        
        Fields (from Docs samples):
        - (no fields listed)"""
        return self.execute("getVendorsToApprove", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def hold(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "hold".
        
        Fields (from Docs samples):
        - CONTRACTDETAIL.ASOFDATE
        - CONTRACTDETAIL.BILLING
        - CONTRACTDETAIL.EXPENSE
        - CONTRACTDETAIL.RECORDNO
        - CONTRACTDETAIL.REVENUE
        - CONTRACTEXPENSE.ASOFDATE
        - CONTRACTEXPENSE.RECORDNO"""
        return self.execute("hold", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def hold_revrecschedule(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "hold_revrecschedule".
        
        Fields (from Docs samples):
        - category
        - memo
        - recordno"""
        return self.execute("hold_revrecschedule", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def inspect(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "inspect".
        
        Fields (from Docs samples):
        - object
        
        Operation attributes:
        - detail"""
        return self.execute("inspect", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def install_app(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "installApp".
        
        Fields (from Docs samples):
        - appxml"""
        return self.execute("installApp", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def lookup(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "lookup".
        
        Fields (from Docs samples):
        - object"""
        return self.execute("lookup", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def my_ach_object(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "MY_ACH_OBJECT".
        
        Fields (from Docs samples):
        - ACHEFTFILE
        - ACHEFTFILE_contenttype
        - ACHEFTFILE_filename"""
        return self.execute("MY_ACH_OBJECT", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def partialupdate_potransaction(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "partialupdate_potransaction".
        
        Fields (from Docs samples):
        - dateposted.day
        - dateposted.month
        - dateposted.year
        
        Operation attributes:
        - key"""
        return self.execute("partialupdate_potransaction", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def post(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "post".
        
        Fields (from Docs samples):
        - CONTRACT.GLPOSTINGDATE
        - CONTRACT.POSTMEMO
        - CONTRACT.RECORDNO
        - CONTRACTDETAIL.GLPOSTINGDATE
        - CONTRACTDETAIL.POSTMEMO
        - CONTRACTDETAIL.RECORDNO
        - CONTRACTEXPENSE.GLPOSTINGDATE
        - CONTRACTEXPENSE.POSTMEMO
        - CONTRACTEXPENSE.RECORDNO
        - CONTRACTEXPENSE2SCHEDULE.ASOFDATE
        - CONTRACTEXPENSE2SCHEDULE.CONTRACTID
        - CONTRACTEXPENSE2SCHEDULE.CUSTOMERID
        - CONTRACTEXPENSE2SCHEDULE.POSTINGDATE
        - CONTRACTEXPENSESCHEDULE.ASOFDATE
        - CONTRACTEXPENSESCHEDULE.CONTRACTID
        - CONTRACTEXPENSESCHEDULE.CUSTOMERID
        - CONTRACTEXPENSESCHEDULE.POSTINGDATE
        - CONTRACTEXPENSESCHEDULEENTRY.POSTINGDATE
        - CONTRACTEXPENSESCHEDULEENTRY.RECORDNO
        - CONTRACTREVENUE2SCHEDULE.ASOFDATE
        - CONTRACTREVENUE2SCHEDULE.CONTRACTID
        - CONTRACTREVENUE2SCHEDULE.CUSTOMERID
        - CONTRACTREVENUE2SCHEDULE.POSTINGDATE
        - CONTRACTREVENUESCHEDULE.ASOFDATE
        - CONTRACTREVENUESCHEDULE.CONTRACTID
        - CONTRACTREVENUESCHEDULE.CUSTOMERID
        - CONTRACTREVENUESCHEDULE.POSTINGDATE
        - CONTRACTREVENUESCHEDULEENTRY.POSTINGDATE
        - CONTRACTREVENUESCHEDULEENTRY.RECORDNO"""
        return self.execute("post", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def post_revrecscheduleentry(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "post_revrecscheduleentry".
        
        Fields (from Docs samples):
        - recordno"""
        return self.execute("post_revrecscheduleentry", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def promote(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "promote".
        
        Fields (from Docs samples):
        - JOBQUEUERECORD.JOBID"""
        return self.execute("promote", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def query(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "query".
        
        Fields (from Docs samples):
        - docparid
        - filter.and.equalto.field
        - filter.and.equalto.value
        - filter.and.isnotnull.field
        - filter.and.like.field
        - filter.and.like.value
        - filter.and.notequalto.field
        - filter.and.notequalto.value
        - filter.between.field
        - filter.between.value
        - filter.equalto.field
        - filter.equalto.value
        - filter.greaterthan.field
        - filter.greaterthan.value
        - filter.greaterthanorequalto.field
        - filter.greaterthanorequalto.value
        - filter.isnotnull.field
        - filter.isnull.field
        - filter.like.field
        - filter.like.value
        - filter.or.equalto.field
        - filter.or.equalto.value
        - object
        - orderby.order.descending
        - orderby.order.field
        - select.field"""
        return self.execute("query", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def read(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "read".
        
        Fields (from Docs samples):
        - ACCTTITLEBYLOC:
          - *
        - ACCUMULATIONTYPE:
          - *
        - ACHBANK:
          - *
        - ACTIVITYLOG:
          - *
        - AFRSETUP:
          - *
        - AISLE:
          - *
        - ALLOCATION:
          - *
        - ALLOCATIONENTRY:
          - *
        - APACCOUNTLABEL:
          - *
        - APADJUSTMENT:
          - *
        - APBILL:
          - *
        - APBILLBATCH:
          - *
        - APBILLITEM:
          - *
        - APBILLJOINTPAYEE:
          - *
        - APPAYMENT:
          - *
        - APPAYMENTREQUEST:
          - *
        - APPYMT:
          - *
        - APPYMTDETAIL:
          - *
        - APRECURBILL:
          - *
        - APRECURBILLENTRY:
          - *
        - APRETAINAGERELEASE:
          - *
        - APRETAINAGERELEASEENTRY:
          - *
        - APTERM:
          - *
        - ARACCOUNTLABEL:
          - *
        - ARADJUSTMENT:
          - *
        - ARADVANCE:
          - *
        - ARINVOICE:
          - *
        - ARINVOICEBATCH:
          - *
        - ARPAYMENT:
          - *
        - ARPYMT:
          - *
        - ARRECURINVOICE:
          - *
        - ARRETAINAGERELEASE:
          - *
        - ARRETAINAGERELEASEENTRY:
          - *
        - ARTERM:
          - *
        - AVAILABLEINVENTORY:
          - *
        - BANKACCTRECON:
          - *
        - BANKACCTTXNFEED:
          - *
        - BANKFEE:
          - *
        - BANKFEEENTRY:
          - *
        - BIN:
          - *
        - BINFACE:
          - *
        - BINSIZE:
          - *
        - CCTRANSACTION:
          - *
        - CCTRANSACTIONENTRY:
          - *
        - CHANGEREQUEST:
          - *
        - CHANGEREQUESTENTRY:
          - *
        - CHANGEREQUESTSTATUS:
          - *
        - CHANGEREQUESTTYPE:
          - *
        - CHARGEPAYOFF:
          - *
        - CHARGEPAYOFFENTRY:
          - *
        - CHECKINGACCOUNT:
          - *
        - CLASS:
          - *
        - CLASSGROUP:
          - *
        - COGSCLOSEDJE:
          - *
        - COMPLIANCEDEFINITION:
          - *
        - COMPLIANCERECORD:
          - *
        - COMPLIANCETYPE:
          - *
        - CONTACT:
          - *
        - CONTRACT:
          - *
        - CONTRACTBILLINGSCHEDULE:
          - *
        - CONTRACTBILLINGSCHEDULEENTRY:
          - *
        - CONTRACTBILLINGTEMPLATE:
          - *
        - CONTRACTBILLINGTEMPLATEENTRY:
          - *
        - CONTRACTDETAIL:
          - *
        - CONTRACTEXPENSE:
          - *
        - CONTRACTEXPENSE2SCHEDULE:
          - *
        - CONTRACTEXPENSESCHEDULE:
          - *
        - CONTRACTEXPENSETEMPLATE:
          - *
        - CONTRACTGROUP:
          - *
        - CONTRACTITEMPRCLSTENTYTIER:
          - *
        - CONTRACTITEMPRICELIST:
          - *
        - CONTRACTITEMPRICELISTENTRY:
          - *
        - CONTRACTMEABUNDLE:
          - *
        - CONTRACTMEAITEMPRICELIST:
          - *
        - CONTRACTMEAITEMPRICELISTENTRY:
          - *
        - CONTRACTMEAPRICELIST:
          - *
        - CONTRACTPRICELIST:
          - *
        - CONTRACTREVENUE2SCHEDULE:
          - *
        - CONTRACTREVENUESCHEDULE:
          - *
        - CONTRACTREVENUETEMPLATE:
          - *
        - CONTRACTTYPE:
          - *
        - CONTRACTUSAGE:
          - *
        - COSTTYPE:
          - *
        - CREDITCARD:
          - *
        - CREDITCARDFEE:
          - *
        - CREDITCARDFEEENTRY:
          - *
        - CUSTOMER:
          - *
        - CUSTOMEREMAILTEMPLATE:
          - *
        - CUSTOMERGROUP:
          - *
        - CUSTOMERVISIBILITY:
          - *
        - CUSTTYPE:
          - *
        - DDSJOB:
          - *
        - DEPARTMENT:
          - *
        - DEPARTMENTGROUP:
          - *
        - DEPOSIT:
          - *
        - DEPOSITENTRY:
          - *
        - DUNNINGDEFINITION:
          - *
        - EARNINGTYPE:
          - *
        - EEACCOUNTLABEL:
          - *
        - EEXPENSES:
          - *
        - EMPLOYEE:
          - *
        - EMPLOYEEGROUP:
          - *
        - EMPLOYEEPOSITION:
          - *
        - EMPLOYEETYPE:
          - *
        - EPPAYMENT:
          - *
        - EPPAYMENTREQUEST:
          - *
        - EXCHANGERATE:
          - *
        - EXCHANGERATEENTRY:
          - *
        - EXCHANGERATETYPES:
          - *
        - EXPENSEADJUSTMENTS:
          - *
        - EXPENSEADJUSTMENTSITEM:
          - *
        - EXPENSEPAYMENTTYPE:
          - *
        - FUNDSTRANSFER:
          - *
        - GCBOOK:
          - *
        - GCBOOKACCTRATETYPE:
          - *
        - GCBOOKADJJOURNAL:
          - *
        - GCBOOKELIMACCOUNT:
          - *
        - GCBOOKENTITY:
          - *
        - GCOWNERSHIPCHILDENTITY:
          - *
        - GCOWNERSHIPENTITY:
          - *
        - GCOWNERSHIPSTRUCTURE:
          - *
        - GCOWNERSHIPSTRUCTUREDETAIL:
          - *
        - GENINVOICEPOLICY:
          - *
        - GENINVOICEPREVIEW:
          - *
        - GENINVOICEPREVIEWLINE:
          - *
        - GENINVOICERUN:
          - *
        - GLACCOUNT:
          - *
        - GLACCTALLOCATION:
          - *
        - GLACCTALLOCATIONGRP:
          - *
        - GLACCTALLOCATIONRUN:
          - *
        - GLACCTGRP:
          - *
        - GLACCTGRPPURPOSE:
          - *
        - GLBATCH:
          - *
        - GLBUDGETHEADER:
          - *
        - GLBUDGETITEM:
          - *
        - GLENTRY:
          - *
        - ICCYCLECOUNT:
          - *
        - ICCYCLECOUNTENTRY:
          - *
        - ICROW:
          - *
        - ICTRANSFER:
          - *
        - INTERENTITYSETUP:
          - *
        - INVDOCUMENT:
          - *
        - INVDOCUMENTENTRY:
          - *
        - INVDOCUMENTPARAMS:
          - *
        - INVDOCUMENTSUBTOTALS:
          - *
        - INVENTORYTOTALDETAIL:
          - *
        - INVENTORYWQDETAIL:
          - DOCID
          - HOLDPROGRESS
          - ICWQORDERID
          - RECORDNO
          - STATUS
        - INVENTORYWQORDER:
          - CUSTOMERID
          - DOCID
          - HOLDPROGRESS
          - PCTFULFILLABLE
          - STATUS
        - INVPRICELIST:
          - *
        - ITEM:
          - *
        - ITEMCROSSREF:
          - *
        - ITEMGLGROUP:
          - *
        - ITEMGROUP:
          - *
        - ITEMTAXGROUP:
          - *
        - ITEMWAREHOUSEINFO:
          - *
        - JOBQUEUERECORD:
          - *
        - LABORCLASS:
          - *
        - LABORSHIFT:
          - *
        - LABORUNION:
          - *
        - LOCATION:
          - *
        - LOCATIONENTITY:
          - *
        - LOCATIONGROUP:
          - *
        - MEMBERUSERGROUP:
          - *
        - OBSPCTCOMPLETED:
          - *
        - OTHERRECEIPTS:
          - *
        - OTHERRECEIPTSENTRY:
          - *
        - PAYROLLREPORTCHECK:
          - *
        - PAYROLLREPORTEMPLOYEE:
          - *
        - PAYROLLREPORTGROSSPAY:
          - *
        - PAYROLLREPORTPAYMODIFIER:
          - *
        - PAYROLLREPORTPTOACCRUALSCHEDULE:
          - *
        - PAYROLLREPORTPTOACTIVITY:
          - *
        - PAYROLLREPORTTAX:
          - *
        - PAYROLLREPORTTAXSETUP:
          - *
        - PAYROLLREPORTTIMECARD:
          - *
        - PAYROLLREPORTTRADE:
          - *
        - PJESTIMATE:
          - *
        - PJESTIMATEENTRY:
          - *
        - PJESTIMATETYPE:
          - *
        - PODOCUMENT:
          - *
        - PODOCUMENTENTRY:
          - *
        - PODOCUMENTPARAMS:
          - *
        - PODOCUMENTSUBTOTALS:
          - *
        - POPRICELIST:
          - *
        - POSITIONSKILL:
          - *
        - POSUBTOTALTEMPLATE:
          - *
        - PRODUCTLINE:
          - *
        - PROJECT:
          - *
        - PROJECTCHANGEORDER:
          - *
        - PROJECTCONTRACT:
          - *
        - PROJECTCONTRACTLINE:
          - *
        - PROJECTCONTRACTLINEENTRY:
          - *
        - PROJECTCONTRACTTYPE:
          - *
        - PROJECTGROUP:
          - *
        - PROJECTRESOURCES:
          - *
        - PROJECTSTATUS:
          - *
        - PROJECTTYPE:
          - *
        - PROVIDERBANKACCOUNT:
          - *
        - PROVIDERPAYMENTMETHOD:
          - *
        - PROVIDERVENDOR:
          - *
        - PTAPPLICATION:
          - *
        - RATETABLE:
          - *
        - RATETABLEAPENTRY:
          - *
        - RATETABLEPOENTRY:
          - *
        - RATETABLETSENTRY:
          - *
        - RECURGLACCTALLOCATION:
          - *
        - REPORTINGPERIOD:
          - *
        - REVRECSCHEDULE:
          - *
        - REVRECSCHEDULEENTRY:
          - *
        - ROLEASSIGNMENT:
          - *
        - ROLEGROUPS:
          - *
        - ROLEPOLICYASSIGNMENT:
          - *
        - ROLES:
          - *
        - ROLEUSERS:
          - *
        - SAVINGSACCOUNT:
          - *
        - SODOCUMENT:
          - *
        - SODOCUMENTENTRY:
          - *
        - SODOCUMENTPARAMS:
          - *
        - SODOCUMENTSUBTOTALS:
          - *
        - SOPRICELIST:
          - *
        - SORECURDOCUMENT:
          - *
        - SOSUBTOTALTEMPLATE:
          - *
        - STANDARDCOSTTYPE:
          - *
        - STANDARDTASK:
          - *
        - STATACCOUNT:
          - *
        - TASK:
          - *
        - TASKRESOURCES:
          - *
        - TAXDETAIL:
          - *
        - TAXRECORD:
          - *
        - TAXSOLUTION:
          - *
        - TIMESHEET:
          - *
        - TIMESHEETAPPROVAL:
          - *
        - TIMESHEETENTRY:
          - *
        - TIMETYPE:
          - *
        - TRANSACTIONRULE:
          - *
        - TRANSACTIONRULEDETAIL:
          - *
        - UOM:
          - *
        - UOMDETAIL:
          - *
        - USERGROUP:
          - *
        - USERINFO:
          - *
        - USERRESTRICTION:
          - *
        - USERRIGHTS:
          - *
        - VENDOR:
          - *
        - VENDOREMAILTEMPLATE:
          - *
        - VENDORGROUP:
          - *
        - VENDORVISIBILITY:
          - *
        - VENDTYPE:
          - *
        - WAREHOUSE:
          - *
        - WAREHOUSEGROUP:
          - *
        - ZONE:
          - *"""
        return self.execute("read", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def read_by_name(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "readByName".
        
        Fields (from Docs samples):
        - ACCUMULATIONTYPE:
          - *
        - ACHBANK:
          - *
        - AISLE:
          - *
        - ALLOCATION:
          - *
        - APACCOUNTLABEL:
          - *
        - APTERM:
          - *
        - ARACCOUNTLABEL:
          - *
        - ARTERM:
          - *
        - BIN:
          - *
        - BINFACE:
          - *
        - BINSIZE:
          - *
        - CHANGEREQUEST:
          - *
        - CHANGEREQUESTSTATUS:
          - *
        - CHANGEREQUESTTYPE:
          - *
        - CHECKINGACCOUNT:
          - *
        - CLASS:
          - *
        - CLASSGROUP:
          - *
        - COMPLIANCEDEFINITION:
          - *
        - COMPLIANCERECORD:
          - *
        - COMPLIANCETYPE:
          - *
        - CONTACT:
          - *
        - CONTRACT:
          - *
        - CONTRACTBILLINGTEMPLATE:
          - *
        - CONTRACTEXPENSETEMPLATE:
          - *
        - CONTRACTGROUP:
          - *
        - CONTRACTMEAPRICELIST:
          - *
        - CONTRACTPRICELIST:
          - *
        - CONTRACTREVENUETEMPLATE:
          - *
        - CONTRACTTYPE:
          - *
        - CREDITCARD:
          - *
        - CUSTOMER:
          - *
        - CUSTOMEREMAILTEMPLATE:
          - *
        - CUSTOMERGROUP:
          - *
        - CUSTTYPE:
          - *
        - DEPARTMENT:
          - *
        - DEPARTMENTGROUP:
          - *
        - EARNINGTYPE:
          - *
        - EEACCOUNTLABEL:
          - *
        - EMPLOYEE:
          - *
        - EMPLOYEEGROUP:
          - *
        - EMPLOYEEPOSITION:
          - *
        - EMPLOYEETYPE:
          - *
        - EXCHANGERATETYPES:
          - *
        - EXPENSEPAYMENTTYPE:
          - *
        - GCBOOK:
          - *
        - GCOWNERSHIPSTRUCTURE:
          - *
        - GLACCOUNT:
          - *
        - GLACCTGRP:
          - *
        - GLACCTGRPPURPOSE:
          - *
        - GLBUDGETHEADER:
          - *
        - ICROW:
          - *
        - INVPRICELIST:
          - *
        - ITEM:
          - *
        - ITEMGLGROUP:
          - *
        - ITEMGROUP:
          - *
        - ITEMTAXGROUP:
          - *
        - LABORCLASS:
          - *
        - LABORSHIFT:
          - *
        - LABORUNION:
          - *
        - LOCATION:
          - *
        - LOCATIONENTITY:
          - *
        - LOCATIONGROUP:
          - *
        - PJESTIMATE:
          - *
        - PJESTIMATETYPE:
          - *
        - POPRICELIST:
          - *
        - POSITIONSKILL:
          - *
        - POSUBTOTALTEMPLATE:
          - *
        - PRODUCTLINE:
          - *
        - PROJECT:
          - *
        - PROJECTCHANGEORDER:
          - *
        - PROJECTCONTRACT:
          - *
        - PROJECTCONTRACTTYPE:
          - *
        - PROJECTGROUP:
          - *
        - PROJECTSTATUS:
          - *
        - PROJECTTYPE:
          - *
        - PTAPPLICATION:
          - *
        - RATETABLE:
          - *
        - REPORTINGPERIOD:
          - *
        - ROLES:
          - *
        - SAVINGSACCOUNT:
          - *
        - SOPRICELIST:
          - *
        - SOSUBTOTALTEMPLATE:
          - *
        - STANDARDCOSTTYPE:
          - *
        - STANDARDTASK:
          - *
        - STATACCOUNT:
          - *
        - TAXSOLUTION:
          - *
        - TIMETYPE:
          - *
        - TRANSACTIONRULE:
          - *
        - UOM:
          - *
        - USERINFO:
          - *
        - VENDOR:
          - *
        - VENDORGROUP:
          - *
        - VENDTYPE:
          - *
        - WAREHOUSE:
          - *
        - WAREHOUSEGROUP:
          - *
        - ZONE:
          - *"""
        return self.execute("readByName", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def read_by_query(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "readByQuery".
        
        Fields (from Docs samples):
        - ACCTTITLEBYLOC:
          - *
        - ACCUMULATIONTYPE:
          - *
        - ACHBANK:
          - *
        - ACTIVITYLOG:
          - *
        - ADVAUDITHISTORY:
          - *
        - AISLE:
          - *
        - ALLOCATION:
          - *
        - ALLOCATIONENTRY:
          - *
        - APACCOUNTLABEL:
          - *
        - APADJUSTMENT:
          - *
        - APADJUSTMENTITEM:
          - *
        - APBILL:
          - *
        - APBILLBATCH:
          - *
        - APBILLITEM:
          - *
        - APBILLJOINTPAYEE:
          - *
        - APPAYMENTREQUEST:
          - *
        - APPYMT:
          - *
        - APPYMTDETAIL:
          - *
        - APRECURBILL:
          - *
        - APRECURBILLENTRY:
          - *
        - APRETAINAGERELEASE:
          - *
        - APRETAINAGERELEASEENTRY:
          - *
        - APTERM:
          - *
        - ARACCOUNTLABEL:
          - *
        - ARADJUSTMENT:
          - *
        - ARADJUSTMENTITEM:
          - *
        - ARADVANCE:
          - *
        - ARINVOICE:
          - *
        - ARINVOICEBATCH:
          - *
        - ARPAYMENT:
          - *
        - ARPYMT:
          - *
        - ARRECURINVOICE:
          - *
        - ARRECURINVOICEENTRY:
          - *
        - ARRETAINAGERELEASEENTRY:
          - *
        - ARTERM:
          - *
        - AUDITHISTORY:
          - *
        - AVAILABLEINVENTORY:
          - *
        - BANKACCTRECON:
          - *
        - BANKACCTTXNFEED:
          - *
        - BANKFEE:
          - *
        - BANKFEEENTRY:
          - *
        - BIN:
          - *
        - BINFACE:
          - *
        - BINSIZE:
          - *
        - CCTRANSACTION:
          - *
        - CCTRANSACTIONENTRY:
          - *
        - CHANGEREQUEST:
          - *
        - CHANGEREQUESTENTRY:
          - *
        - CHANGEREQUESTSTATUS:
          - *
        - CHANGEREQUESTTYPE:
          - *
        - CHARGEPAYOFF:
          - *
        - CHARGEPAYOFFENTRY:
          - *
        - CHECKINGACCOUNT:
          - *
        - CLASS:
          - *
        - CLASSGROUP:
          - *
        - COGSCLOSEDJE:
          - *
        - COMPLIANCEDEFINITION:
          - ALLOWNEGATIVELIENWAIVERS
          - COMPLIANCEDEFINITIONID
          - NAME
          - RECORDNO
        - COMPLIANCETYPE:
          - COMPLIANCETEMPLATE
          - COMPLIANCETYPEID
          - FINALCOMPLIANCETEMPLATE
          - NAME
          - RECORDNO
          - STATUS
        - CONTACT:
          - *
        - CONTRACT:
          - *
        - CONTRACTBILLINGSCHEDULE:
          - *
        - CONTRACTBILLINGSCHEDULEENTRY:
          - *
        - CONTRACTBILLINGTEMPLATE:
          - *
        - CONTRACTBILLINGTEMPLATEENTRY:
          - *
        - CONTRACTDETAIL:
          - *
        - CONTRACTEXPENSE:
          - *
        - CONTRACTEXPENSE2SCHEDULE:
          - *
        - CONTRACTEXPENSESCHEDULE:
          - *
        - CONTRACTEXPENSETEMPLATE:
          - *
        - CONTRACTGROUP:
          - *
        - CONTRACTITEMPRCLSTENTYTIER:
          - *
        - CONTRACTITEMPRICELIST:
          - *
        - CONTRACTITEMPRICELISTENTRY:
          - *
        - CONTRACTMEABUNDLE:
          - *
        - CONTRACTMEAITEMPRICELIST:
          - *
        - CONTRACTMEAITEMPRICELISTENTRY:
          - *
        - CONTRACTMEAPRICELIST:
          - *
        - CONTRACTPRICELIST:
          - *
        - CONTRACTREVENUE2SCHEDULE:
          - *
        - CONTRACTREVENUESCHEDULE:
          - *
        - CONTRACTREVENUETEMPLATE:
          - *
        - CONTRACTTYPE:
          - *
        - CONTRACTUSAGE:
          - *
        - COSTTYPE:
          - *
        - CREDITCARD:
          - *
        - CREDITCARDFEE:
          - *
        - CREDITCARDFEEENTRY:
          - *
        - CUSTOMER:
          - *
        - CUSTOMEREMAILTEMPLATE:
          - *
        - CUSTOMERGROUP:
          - *
        - CUSTTYPE:
          - *
        - DDSJOB:
          - *
        - DEPARTMENT:
          - *
        - DEPARTMENTGROUP:
          - *
        - DEPOSIT:
          - *
        - DEPOSITENTRY:
          - *
        - EARNINGTYPE:
          - *
        - EEACCOUNTLABEL:
          - *
        - EEXPENSES:
          - *
        - EMPLOYEE:
          - *
        - EMPLOYEEGROUP:
          - *
        - EMPLOYEEPOSITION:
          - *
        - EMPLOYEETYPE:
          - *
        - EPPAYMENT:
          - *
        - EPPAYMENTREQUEST:
          - *
        - EXCHANGERATE:
          - *
        - EXCHANGERATEENTRY:
          - *
        - EXCHANGERATETYPES:
          - *
        - EXPENSEADJUSTMENTS:
          - *
        - EXPENSEADJUSTMENTSITEM:
          - *
        - EXPENSEPAYMENTTYPE:
          - *
        - FUNDSTRANSFER:
          - *
        - FUNDSTRANSFERENTRY:
          - *
        - GCBOOK:
          - *
        - GCBOOKACCTRATETYPE:
          - *
        - GCBOOKADJJOURNAL:
          - *
        - GCBOOKELIMACCOUNT:
          - *
        - GCBOOKENTITY:
          - *
        - GENINVOICEPOLICY:
          - *
        - GENINVOICEPREVIEW:
          - *
        - GENINVOICEPREVIEWLINE:
          - *
        - GENINVOICERUN:
          - *
        - GLACCOUNT:
          - *
        - GLACCOUNTBALANCE:
          - *
        - GLACCTALLOCATION:
          - *
        - GLACCTALLOCATIONGRP:
          - *
        - GLACCTALLOCATIONRUN:
          - *
        - GLACCTGRP:
          - *
        - GLACCTGRPHIERARCHY:
          - *
        - GLACCTGRPPURPOSE:
          - *
        - GLBATCH:
          - *
        - GLBUDGETHEADER:
          - *
        - GLBUDGETITEM:
          - *
        - GLDETAIL:
          - *
        - GLENTRY:
          - *
        - ICCYCLECOUNT:
          - *
        - ICCYCLECOUNTENTRY:
          - *
        - ICROW:
          - *
        - ICTRANSFER:
          - *
        - INVDOCUMENT:
          - *
        - INVDOCUMENTENTRY:
          - *
        - INVDOCUMENTPARAMS:
          - *
        - INVDOCUMENTSUBTOTALS:
          - *
        - INVENTORYTOTALDETAIL:
          - *
        - INVENTORYWQDETAIL:
          - DOCID
          - HOLDPROGRESS
          - ICWQORDERID
          - RECORDNO
        - INVENTORYWQORDER:
          - CUSTOMERID
          - ICWQORDERID
          - PCTFULFILLABLE
          - STATUS
        - INVPRICELIST:
          - *
        - ITEM:
          - *
        - ITEMCROSSREF:
          - *
        - ITEMGLGROUP:
          - *
        - ITEMGROUP:
          - *
        - ITEMTAXGROUP:
          - *
        - ITEMWAREHOUSEINFO:
          - *
        - JOBQUEUERECORD:
          - *
        - LABORCLASS:
          - *
        - LABORSHIFT:
          - *
        - LABORUNION:
          - *
        - LOCATION:
          - *
        - LOCATIONENTITY:
          - *
        - LOCATIONGROUP:
          - *
        - MEMBERUSERGROUP:
          - *
        - OBSPCTCOMPLETED:
          - *
        - OTHERRECEIPTS:
          - *
        - OTHERRECEIPTSENTRY:
          - *
        - PJESTIMATE:
          - *
        - PJESTIMATEENTRY:
          - *
        - PJESTIMATETYPE:
          - *
        - PODOCUMENT:
          - *
        - PODOCUMENTENTRY:
          - *
        - PODOCUMENTPARAMS:
          - *
        - PODOCUMENTSUBTOTALS:
          - *
        - POPRICELIST:
          - *
        - POSITIONSKILL:
          - *
        - POSUBTOTALTEMPLATE:
          - *
        - PRODUCTLINE:
          - *
        - PROJECT:
          - *
        - PROJECTCHANGEORDER:
          - *
        - PROJECTGROUP:
          - *
        - PROJECTRESOURCES:
          - *
        - PROJECTSTATUS:
          - *
        - PROJECTTYPE:
          - *
        - PROVIDERBANKACCOUNT:
          - *
        - PROVIDERPAYMENTMETHOD:
          - *
        - PROVIDERVENDOR:
          - *
        - PTAPPLICATION:
          - *
        - RECURGLACCTALLOCATION:
          - *
        - REPORTINGPERIOD:
          - *
        - REVRECSCHEDULE:
          - *
        - REVRECSCHEDULEENTRY:
          - *
        - ROLEASSIGNMENT:
          - *
        - ROLEGROUPS:
          - *
        - ROLEPOLICYASSIGNMENT:
          - *
        - ROLES:
          - *
        - ROLEUSERS:
          - *
        - SAVINGSACCOUNT:
          - *
        - SODOCUMENT:
          - *
        - SODOCUMENTENTRY:
          - *
        - SODOCUMENTPARAMS:
          - *
        - SODOCUMENTSUBTOTALS:
          - *
        - SOPRICELIST:
          - *
        - SORECURDOCUMENT:
          - *
        - SOSUBTOTALTEMPLATE:
          - *
        - STANDARDCOSTTYPE:
          - *
        - STANDARDTASK:
          - *
        - STATACCOUNT:
          - *
        - TASK:
          - *
        - TASKRESOURCES:
          - *
        - TAXDETAIL:
          - (no fields listed)
        - TAXRECORD:
          - *
        - TAXSOLUTION:
          - *
        - TIMESHEET:
          - *
        - TIMESHEETENTRY:
          - *
        - TIMETYPE:
          - *
        - TRANSACTIONRULE:
          - *
        - TRANSACTIONRULEDETAIL:
          - *
        - UOM:
          - *
        - UOMDETAIL:
          - *
        - USERGROUP:
          - *
        - USERINFO:
          - *
        - USERRESTRICTION:
          - *
        - USERRIGHTS:
          - *
        - USERROLES:
          - *
        - VENDOR:
          - *
        - VENDOREMAILTEMPLATE:
          - *
        - VENDORGROUP:
          - *
        - VENDTYPE:
          - *
        - WAREHOUSE:
          - *
        - WAREHOUSEGROUP:
          - *
        - ZONE:
          - *"""
        return self.execute("readByQuery", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def read_entity_details(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "readEntityDetails".
        
        Fields (from Docs samples):
        - (no fields listed)"""
        return self.execute("readEntityDetails", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def read_more(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "readMore".
        
        Fields (from Docs samples):
        - reportId"""
        return self.execute("readMore", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def read_related(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "readRelated".
        
        Fields (from Docs samples):
        - fields
        - keys
        - object
        - relation"""
        return self.execute("readRelated", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def read_report(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "readReport".
        
        Fields (from Docs samples):
        - arguments.APBILL.TEST_DATE.FROM_DATE
        - arguments.APBILL.TEST_DATE.TO_DATE
        - arguments.AP_RECORD.WHENCREATED
        - arguments.get_accountbalancesbydimensions.endaccountno
        - arguments.get_accountbalancesbydimensions.enddate.day
        - arguments.get_accountbalancesbydimensions.enddate.month
        - arguments.get_accountbalancesbydimensions.enddate.year
        - arguments.get_accountbalancesbydimensions.groupby
        - arguments.get_accountbalancesbydimensions.locationid
        - arguments.get_accountbalancesbydimensions.startaccountno
        - arguments.get_accountbalancesbydimensions.startdate.day
        - arguments.get_accountbalancesbydimensions.startdate.month
        - arguments.get_accountbalancesbydimensions.startdate.year
        - pagesize
        - report
        - waitTime
        
        Operation attributes:
        - returnDef
        - type"""
        return self.execute("readReport", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def read_user_formatting(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "readUserFormatting".
        
        Fields (from Docs samples):
        - key"""
        return self.execute("readUserFormatting", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def read_view(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "readView".
        
        Fields (from Docs samples):
        - filters.filterCondition
        - filters.filterExpression.field
        - filters.filterExpression.operator
        - filters.filterExpression.value
        - pagesize
        - view"""
        return self.execute("readView", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def reallocate(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "reallocate".
        
        Fields (from Docs samples):
        - CONTRACTEXPENSE2SCHEDULE.ENDDATE
        - CONTRACTEXPENSE2SCHEDULE.SCHEDULEKEY
        - CONTRACTEXPENSE2SCHEDULE.STARTDATE
        - CONTRACTEXPENSESCHEDULE.ENDDATE
        - CONTRACTEXPENSESCHEDULE.SCHEDULEKEY
        - CONTRACTEXPENSESCHEDULE.STARTDATE
        - CONTRACTREVENUE2SCHEDULE.ENDDATE
        - CONTRACTREVENUE2SCHEDULE.SCHEDULEKEY
        - CONTRACTREVENUE2SCHEDULE.STARTDATE
        - CONTRACTREVENUESCHEDULE.ENDDATE
        - CONTRACTREVENUESCHEDULE.SCHEDULEKEY
        - CONTRACTREVENUESCHEDULE.STARTDATE"""
        return self.execute("reallocate", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def reallocate_revrecschedule(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "reallocate_revrecschedule".
        
        Fields (from Docs samples):
        - recordno
        - revrecenddate.day
        - revrecenddate.month
        - revrecenddate.year
        - revrecstartdate.day
        - revrecstartdate.month
        - revrecstartdate.year"""
        return self.execute("reallocate_revrecschedule", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def reconcile_bank(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "reconcile_bank".
        
        Fields (from Docs samples):
        - bankaccountid
        - banktxns.banktxn.amount
        - banktxns.banktxn.description
        - banktxns.banktxn.doctype
        - banktxns.banktxn.document
        - banktxns.banktxn.payee
        - banktxns.banktxn.postingdate.day
        - banktxns.banktxn.postingdate.month
        - banktxns.banktxn.postingdate.year
        - banktxns.banktxn.txntype
        - cutoffdate.day
        - cutoffdate.month
        - cutoffdate.year
        - reconmode
        - statementendingbalance
        - statementendingdate.day
        - statementendingdate.month
        - statementendingdate.year"""
        return self.execute("reconcile_bank", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def record_cctransaction(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "record_cctransaction".
        
        Fields (from Docs samples):
        - ccpayitems.ccpayitem.classid
        - ccpayitems.ccpayitem.contractid
        - ccpayitems.ccpayitem.customerid
        - ccpayitems.ccpayitem.departmentid
        - ccpayitems.ccpayitem.description
        - ccpayitems.ccpayitem.employeeid
        - ccpayitems.ccpayitem.glaccountno
        - ccpayitems.ccpayitem.itemid
        - ccpayitems.ccpayitem.locationid
        - ccpayitems.ccpayitem.paymentamount
        - ccpayitems.ccpayitem.projectid
        - ccpayitems.ccpayitem.vendorid
        - ccpayitems.ccpayitem.warehouseid
        - chargecardid
        - currency
        - description
        - exchratetype
        - payee
        - paymentdate.day
        - paymentdate.month
        - paymentdate.year
        - referenceno
        - supdocid"""
        return self.execute("record_cctransaction", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def record_deposit(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "record_deposit".
        
        Fields (from Docs samples):
        - bankaccountid
        - customfields.customfield.customfieldname
        - customfields.customfield.customfieldvalue
        - depositdate.day
        - depositdate.month
        - depositdate.year
        - depositid
        - description
        - receiptkeys.receiptkey
        - supdocid"""
        return self.execute("record_deposit", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def record_otherreceipt(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "record_otherreceipt".
        
        Fields (from Docs samples):
        - bankaccountid
        - depositdate.day
        - depositdate.month
        - depositdate.year
        - description
        - payee
        - paymentdate.day
        - paymentdate.month
        - paymentdate.year
        - paymentmethod
        - receiptitems.lineitem.amount
        - receiptitems.lineitem.departmentid
        - receiptitems.lineitem.glaccountno
        - receiptitems.lineitem.locationid
        - receiptitems.lineitem.memo
        - receiveddate.day
        - receiveddate.month
        - receiveddate.year
        - refid"""
        return self.execute("record_otherreceipt", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def renew(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "renew".
        
        Fields (from Docs samples):
        - CONTRACT.CONTRACTID"""
        return self.execute("renew", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def resume(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "resume".
        
        Fields (from Docs samples):
        - CONTRACTDETAIL.ASOFDATE
        - CONTRACTDETAIL.BILLING
        - CONTRACTDETAIL.EXPENSE
        - CONTRACTDETAIL.RECORDNO
        - CONTRACTDETAIL.REVENUE
        - CONTRACTEXPENSE.ASOFDATE
        - CONTRACTEXPENSE.RECORDNO"""
        return self.execute("resume", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def resume_revrecschedule(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "resume_revrecschedule".
        
        Fields (from Docs samples):
        - adjustpostingday
        - memo
        - recordno"""
        return self.execute("resume_revrecschedule", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def retrievepdf(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "retrievepdf".
        
        Fields (from Docs samples):
        - ARINVOICE.RECORDNO
        - SODOCUMENT.DOCID"""
        return self.execute("retrievepdf", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def reverse_appayment(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "reverse_appayment".
        
        Fields (from Docs samples):
        - datereversed.day
        - datereversed.month
        - datereversed.year
        
        Operation attributes:
        - key"""
        return self.execute("reverse_appayment", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def reverse_arpayment(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "reverse_arpayment".
        
        Fields (from Docs samples):
        - datereversed.day
        - datereversed.month
        - datereversed.year
        
        Operation attributes:
        - key"""
        return self.execute("reverse_arpayment", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def reverse_bill(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "reverse_bill".
        
        Fields (from Docs samples):
        - datereversed.day
        - datereversed.month
        - datereversed.year
        
        Operation attributes:
        - key"""
        return self.execute("reverse_bill", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def reverse_cctransaction(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "reverse_cctransaction".
        
        Fields (from Docs samples):
        - datereversed.day
        - datereversed.month
        - datereversed.year
        - memo
        
        Operation attributes:
        - key"""
        return self.execute("reverse_cctransaction", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def reverse_expensereport(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "reverse_expensereport".
        
        Fields (from Docs samples):
        - datereversed.day
        - datereversed.month
        - datereversed.year
        
        Operation attributes:
        - key"""
        return self.execute("reverse_expensereport", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def reverse_invoice(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "reverse_invoice".
        
        Fields (from Docs samples):
        - datereversed.day
        - datereversed.month
        - datereversed.year
        
        Operation attributes:
        - key"""
        return self.execute("reverse_invoice", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def run_dds_job(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "runDdsJob".
        
        Fields (from Docs samples):
        - cloudDelivery
        - jobType
        - object"""
        return self.execute("runDdsJob", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def send_appaymentrequest(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "send_appaymentrequest".
        
        Fields (from Docs samples):
        - appaymentkeys.appaymentkey"""
        return self.execute("send_appaymentrequest", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def terminate_revrecschedule(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "terminate_revrecschedule".
        
        Fields (from Docs samples):
        - category
        - memo
        - recordno"""
        return self.execute("terminate_revrecschedule", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def unpost(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "unpost".
        
        Fields (from Docs samples):
        - CONTRACTEXPENSESCHEDULEENTRY.RECORDNO
        - CONTRACTREVENUESCHEDULEENTRY.RECORDNO"""
        return self.execute("unpost", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def unpost_revrecscheduleentry(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "unpost_revrecscheduleentry".
        
        Fields (from Docs samples):
        - recordno"""
        return self.execute("unpost_revrecscheduleentry", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update".
        
        Fields (from Docs samples):
        - ACCUMULATIONTYPE:
          - RECORDNO
          - STATUS
        - AFRSETUP:
          - DISABLEDELETE
        - ALLOCATION:
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
          - TYPE
        - APACCOUNTLABEL:
          - DESCRIPTION
          - GLACCOUNTNO
          - OFFSETGLACCOUNTNO
          - RECORDNO
          - STATUS
        - APBILL:
          - DESCRIPTION
          - RECORDNO
        - APBILLJOINTPAYEE:
          - JOINTPAYEENAME
          - JOINTPAYEEPRINTAS
          - RECORDNO
        - APPYMT:
          - APPYMTDETAILS.APPYMTDETAIL.ENTRYKEY
          - APPYMTDETAILS.APPYMTDETAIL.RECORDKEY
          - APPYMTDETAILS.APPYMTDETAIL.TRX_PAYMENTAMOUNT
          - RECORDNO
          - WHENCREATED
        - APRETAINAGERELEASE:
          - APRETAINAGERELEASEENTRIES.APRETAINAGERELEASEENTRY.RETAINAGEINVOICEITEMKEY
          - APRETAINAGERELEASEENTRIES.APRETAINAGERELEASEENTRY.RETAINAGEINVOICEKEY
          - APRETAINAGERELEASEENTRIES.APRETAINAGERELEASEENTRY.TRX_AMOUNTRELEASED
          - RECORDNO
        - ARACCOUNTLABEL:
          - DESCRIPTION
          - GLACCOUNTNO
          - OFFSETGLACCOUNTNO
          - RECORDNO
          - STATUS
        - ARADVANCE:
          - DESCRIPTION
          - RECORDNO
        - ARPYMT:
          - ACTION
          - RECORDNO
        - ARRETAINAGERELEASE:
          - ARRETAINAGERELEASEENTRIES.ARRETAINAGERELEASEENTRY.RETAINAGEINVOICEITEMKEY
          - ARRETAINAGERELEASEENTRIES.ARRETAINAGERELEASEENTRY.RETAINAGEINVOICEKEY
          - ARRETAINAGERELEASEENTRIES.ARRETAINAGERELEASEENTRY.TRX_AMOUNTRELEASED
          - RECORDNO
        - BIN:
          - BINID
          - STATUS
        - BINFACE:
          - FACEDESC
          - FACEID
        - BINSIZE:
          - BINDESC
          - RECORDNO
        - CHANGEREQUEST:
          - CHANGEREQUESTSTATUSNAME
          - RECORDNO
        - CHANGEREQUESTSTATUS:
          - RECORDNO
          - WFTYPE
        - CHANGEREQUESTTYPE:
          - RECORDNO
          - STATUS
        - CLASS:
          - NAME
          - RECORDNO
        - COMPLIANCEDEFINITION:
          - COMPDEFENTRIES.DOCPARID
          - COMPLIANCEDEFINITIONID
          - MINLIENWAIVERAMOUNT
          - MINPRIMARYDOCAMOUNT
          - PAYMENTNOTIFICATION
        - COMPLIANCERECORD:
          - DESCRIPTION
          - NOTES
          - PROJECTID
          - RECORDNO
        - COMPLIANCETYPE:
          - description
          - recordno
        - CONTACT:
          - PRINTAS
          - RECORDNO
        - CONTRACT:
          - CONTRACTID
          - DEPARTMENTID
          - NAME
        - CONTRACTBILLINGSCHEDULE:
          - CONTRACTBILLINGSCHEDULEENTRIES.CONTRACTBILLINGSCHEDULEENTRY.POSTINGDATE
          - CONTRACTBILLINGSCHEDULEENTRIES.CONTRACTBILLINGSCHEDULEENTRY.RECORDNO
          - RECORDNO
        - CONTRACTBILLINGTEMPLATE:
          - DESCRIPTION
          - NAME
        - CONTRACTDETAIL:
          - DEPARTMENTID
          - RECORDNO
        - CONTRACTEXPENSE:
          - DEPARTMENTID
          - RECORDNO
        - CONTRACTEXPENSETEMPLATE:
          - DESCRIPTION
          - NAME
        - CONTRACTPRICELIST:
          - DESCRIPTION
          - NAME
        - CONTRACTREVENUETEMPLATE:
          - DESCRIPTION
          - NAME
        - CONTRACTTYPE:
          - RECORDNO
          - STATUS
        - CONTRACTUSAGE:
          - QUANTITY
          - RECORDNO
          - USAGEDATE
        - COSTTYPE:
          - ACTUALBEGINDATE
          - RECORDNO
        - CUSTOMER:
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
          - TERRITORYID
        - DEPARTMENT:
          - CUSTTITLE
          - PARENTID
          - RECORDNO
          - STATUS
          - SUPERVISORID
          - TITLE
        - DUNNINGDEFINITION:
          - CURRENCY
          - DUNNINGDEFINITIONID
          - EMAILTEMPLATEKEY
          - MAXAMOUNT
          - MAXDAYS
          - MINAMOUNT
          - MINDAYS
          - NOTICESEQUENCE
          - PRINTTEMPLATENAME
          - RECORDNO
        - EEACCOUNTLABEL:
          - DESCRIPTION
          - GLACCOUNTNO
          - OFFSETGLACCOUNTNO
          - RECORDNO
          - STATUS
        - EMPLOYEE:
          - RECORDNO
          - TITLE
        - EMPLOYEEPOSITION:
          - NAME
          - RECORDNO
        - GCBOOK:
          - BOOKID
          - BUDGETID
          - DESCRIPTION
        - GCBOOKACCTRATETYPE:
          - GCBOOKACCTRATETYPE.GLACCOUNTNO
          - GCBOOKACCTRATETYPE.GLACCTRATETYPES
          - GCBOOKACCTRATETYPE.OVERRIDEEXPIRYDATE
          - GCBOOKACCTRATETYPE.OVERRIDERATE
          - GCBOOKACCTRATETYPE.RECORDNO
        - GCBOOKADJJOURNAL:
          - RECORDNO
          - TITLE
        - GCOWNERSHIPSTRUCTURE:
          - DESCRIPTION
          - RECORDNO
        - GENINVOICEPOLICY:
          - CONTRACTID
          - INCLUDECONTRACTS
          - RECORDNO
          - SCHEDULED
        - GLACCOUNT:
          - RECORDNO
          - TITLE
        - GLACCTALLOCATION:
          - GLACCTALLOCATIONBASIS.SKIPNEGATIVE
          - RECORDNO
        - GLACCTALLOCATIONGRP:
          - GLACCTALLOCATIONGRPMEMBERS.GLACCTALLOCATIONGRPMEMBER.GLACCTALLOCATIONID
          - RECORDNO
        - GLACCTGRP:
          - GLACCTRANGES.ACCTRANGE.RANGEFROM
          - GLACCTRANGES.ACCTRANGE.RANGETO
          - RECORDNO
          - TITLE
          - TOTALTITLE
        - GLACCTGRPPURPOSE:
          - RECORDNO
          - STATUS
        - GLBATCH:
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
          - REVERSEDATE
        - GLBUDGETHEADER:
          - GLBUDGETITEMS.GLBUDGETITEM.ACCT_NO
          - GLBUDGETITEMS.GLBUDGETITEM.AMOUNT
          - GLBUDGETITEMS.GLBUDGETITEM.DEPT_NO
          - GLBUDGETITEMS.GLBUDGETITEM.LOCATION_NO
          - GLBUDGETITEMS.GLBUDGETITEM.PERIODNAME
          - GLBUDGETITEMS.GLBUDGETITEM.RECORDNO
          - RECORDNO
        - ICCYCLECOUNTENTRY:
          - ADJUSTMENTREASON
          - COUNTEDBYID
          - QUANTITYCOUNTED
          - QUANTITYDAMAGED
          - RECORDNO
        - ICTRANSFER:
          - ACTION
          - DESCRIPTION
          - ICTRANSFERITEMS.ICTRANSFERITEM.IN_OUT
          - ICTRANSFERITEMS.ICTRANSFERITEM.ITEMID
          - ICTRANSFERITEMS.ICTRANSFERITEM.LOCATIONID
          - ICTRANSFERITEMS.ICTRANSFERITEM.QUANTITY
          - ICTRANSFERITEMS.ICTRANSFERITEM.UNIT
          - ICTRANSFERITEMS.ICTRANSFERITEM.WAREHOUSEID
          - RECORDNO
        - INTERENTITYSETUP:
          - ENTITYACCTDEFAULTS.ENTITYACCTDEFAULT.ENTITYID
          - ENTITYACCTDEFAULTS.ENTITYACCTDEFAULT.IEPAYABLEACCTNO
          - ENTITYACCTDEFAULTS.ENTITYACCTDEFAULT.IERECEIVABLEACCTNO
          - ENTITYACCTDEFAULTS.ENTITYACCTDEFAULT.RECORDNO
          - RECORDNO
        - ITEM:
          - NAME
          - RECORDNO
        - ITEMCROSSREF:
          - ITEMALIASDESC
          - RECORDNO
        - LABORCLASS:
          - LABORCLASSID
          - NAME
        - LABORSHIFT:
          - DESCRIPTION
          - LABORSHIFTID
        - LABORUNION:
          - DESCRIPTION
          - LABORUNIONID
        - LOCATION:
          - CONTACTINFO.CONTACTNAME
          - CUSTTITLE
          - ENDDATE
          - NAME
          - PARENTID
          - RECORDNO
          - SHIPTO.CONTACTNAME
          - STARTDATE
          - STATUS
          - SUPERVISORID
        - OBSPCTCOMPLETED:
          - PERCENT
          - RECORDNO
        - PAYROLLREPORTCHECK:
          - CHECKSTATUS
          - RECORDNO
          - REVISIONNUMBER
        - PAYROLLREPORTEMPLOYEE:
          - ACCEPTSELECTRONICW2
          - PAYGROUPID
          - RECORDNO
        - PAYROLLREPORTGROSSPAY:
          - HOURS
          - RECORDNO
        - PAYROLLREPORTPAYMODIFIER:
          - PRETAXCATCHUPCONTRIBUTIONAMT
          - PRETAXCONTRIBUTIONAMT
        - PAYROLLREPORTPTOACCRUALSCHEDULE:
          - PTOTYPEID
          - RECORDNO
        - PAYROLLREPORTPTOACTIVITY:
          - HOURS
          - RECORDNO
        - PAYROLLREPORTTAX:
          - EMPLOYEETAXAMOUNT
          - EMPLOYERTAXAMOUNT
          - RECORDNO
        - PAYROLLREPORTTAXSETUP:
          - RECORDNO
          - TAXCATEGORYID
        - PAYROLLREPORTTIMECARD:
          - RECORDNO
          - WORKDATE
        - PAYROLLREPORTTRADE:
          - RECORDNO
          - TRADEID
        - PJESTIMATE:
          - DESCRIPTION
          - RECORDNO
        - PJESTIMATEENTRY:
          - AMOUNT
          - RECORDNO
          - WFTYPE
        - PJESTIMATETYPE:
          - NAME
          - SELECTEDWFTYPES
        - PROJECT:
          - NAME
          - PROJECTID
        - PROJECTCHANGEORDER:
          - CHANGEREQUESTSTATUSNAME
          - PROJECTCHANGEORDERID
        - PROJECTCONTRACT:
          - RECORDNO
          - STATUS
        - PROJECTCONTRACTLINE:
          - RECORDNO
          - STATUS
        - PROJECTCONTRACTTYPE:
          - PROJECTCONTRACTTYPE
          - STATUS
        - PROVIDERBANKACCOUNT:
          - RECORDNO
          - STATUS
        - PROVIDERVENDOR:
          - RECORDNO
          - STATUS
        - RATETABLE:
          - RATETABLECCENTRIES.RATETABLECCENTRY.ACCUMULATIONTYPENAME
          - RATETABLECCENTRIES.RATETABLECCENTRY.DESCRIPTION
          - RATETABLECCENTRIES.RATETABLECCENTRY.EMPLOYEEID
          - RATETABLECCENTRIES.RATETABLECCENTRY.ITEMID
          - RATETABLECCENTRIES.RATETABLECCENTRY.MARKUPPCT
          - RATETABLECCENTRIES.RATETABLECCENTRY.STANDARDCOSTTYPEID
          - RATETABLECCENTRIES.RATETABLECCENTRY.STANDARDTASKID
          - RATETABLECCENTRIES.RATETABLECCENTRY.STARTDATE
          - RATETABLEID
        - REPORTINGPERIOD:
          - BUDGETING
          - END_DATE
          - HEADER1
          - HEADER2
          - RECORDNO
          - START_DATE
          - STATUS
        - STANDARDCOSTTYPE:
          - DESCRIPTION
          - STANDARDCOSTTYPEID
        - STANDARDTASK:
          - STANDARDTASKID
          - TIMETYPENAME
        - STATACCOUNT:
          - RECORDNO
          - TITLE
        - TASK:
          - PROJECTID
          - RECORDNO
        - TAXRECORD:
          - MCA_NOTES
          - RECORDNO
        - TIMESHEET:
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
          - TIMESHEETENTRIES.TIMESHEETENTRY.VENDORID
        - USERINFO:
          - RECORDNO
          - USERDEPARTMENTS.DEPARTMENTID
          - USERLOCATIONS.LOCATIONID
        - VENDOR:
          - RECORDNO
          - TERMNAME
          - VCF_BILL_SITEID3
        - WAREHOUSE:
          - RECORDNO
          - STATUS
        - ZONE:
          - RECORDNO
          - ZONEDESC"""
        return self.execute("update", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_achbankconfiguration(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_achbankconfiguration".
        
        Fields (from Docs samples):
        - destinationid
        - destinationname
        - eofmarker
        - originid
        - originname
        - referencecode
        - status
        
        Operation attributes:
        - achbankid"""
        return self.execute("update_achbankconfiguration", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_apaccountlabel(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_apaccountlabel".
        
        Fields (from Docs samples):
        - glaccountno
        
        Operation attributes:
        - accountlabel"""
        return self.execute("update_apaccountlabel", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_apadjustment(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_apadjustment".
        
        Fields (from Docs samples):
        - action
        - adjustmentno
        - billno
        - currency
        - datecreated.day
        - datecreated.month
        - datecreated.year
        - dateposted.day
        - dateposted.month
        - dateposted.year
        - description
        - exchratedate.day
        - exchratedate.month
        - exchratedate.year
        - exchratetype
        - updateapadjustmentitems.lineitem.amount
        - updateapadjustmentitems.lineitem.classid
        - updateapadjustmentitems.lineitem.customerid
        - updateapadjustmentitems.lineitem.customfields.customfield.customfieldname
        - updateapadjustmentitems.lineitem.customfields.customfield.customfieldvalue
        - updateapadjustmentitems.lineitem.departmentid
        - updateapadjustmentitems.lineitem.employeeid
        - updateapadjustmentitems.lineitem.glaccountno
        - updateapadjustmentitems.lineitem.itemid
        - updateapadjustmentitems.lineitem.key
        - updateapadjustmentitems.lineitem.locationid
        - updateapadjustmentitems.lineitem.memo
        - updateapadjustmentitems.lineitem.offsetglaccountno
        - updateapadjustmentitems.lineitem.projectid
        - updateapadjustmentitems.lineitem.vendorid
        - updateapadjustmentitems.lineitem.warehouseid
        - vendorid
        
        Operation attributes:
        - key"""
        return self.execute("update_apadjustment", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_apterm(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_apterm".
        
        Fields (from Docs samples):
        - description
        
        Operation attributes:
        - name"""
        return self.execute("update_apterm", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_araccountlabel(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_araccountlabel".
        
        Fields (from Docs samples):
        - glaccountno
        
        Operation attributes:
        - accountlabel"""
        return self.execute("update_araccountlabel", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_aradjustment(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_aradjustment".
        
        Fields (from Docs samples):
        - action
        - adjustmentno
        - currency
        - customerid
        - datecreated.day
        - datecreated.month
        - datecreated.year
        - dateposted.day
        - dateposted.month
        - dateposted.year
        - description
        - exchratetype
        - invoiceno
        - updatearadjustmentitems.lineitem.amount
        - updatearadjustmentitems.lineitem.departmentid
        - updatearadjustmentitems.lineitem.glaccountno
        - updatearadjustmentitems.lineitem.locationid
        - updatearadjustmentitems.lineitem.memo
        - updatearadjustmentitems.updatelineitem.amount
        - updatearadjustmentitems.updatelineitem.departmentid
        - updatearadjustmentitems.updatelineitem.glaccountno
        - updatearadjustmentitems.updatelineitem.locationid
        - updatearadjustmentitems.updatelineitem.memo
        
        Operation attributes:
        - key"""
        return self.execute("update_aradjustment", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_arterm(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_arterm".
        
        Fields (from Docs samples):
        - description
        
        Operation attributes:
        - name"""
        return self.execute("update_arterm", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_bill(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_bill".
        
        Fields (from Docs samples):
        - updatebillitems.updatelineitem.glaccountno
        
        Operation attributes:
        - key"""
        return self.execute("update_bill", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_cctransaction(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_cctransaction".
        
        Fields (from Docs samples):
        - currency
        - description
        - exchratetype
        - payee
        - paymentdate.day
        - paymentdate.month
        - paymentdate.year
        - updateccpayitems.updateccpayitem.description
        - updateccpayitems.updateccpayitem.glaccountno
        - updateccpayitems.updateccpayitem.paymentamount
        
        Operation attributes:
        - key"""
        return self.execute("update_cctransaction", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_class(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_class".
        
        Fields (from Docs samples):
        - name
        
        Operation attributes:
        - key"""
        return self.execute("update_class", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_contact(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_contact".
        
        Fields (from Docs samples):
        - printas
        
        Operation attributes:
        - contactname"""
        return self.execute("update_contact", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_customer(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_customer".
        
        Fields (from Docs samples):
        - name
        - termname
        
        Operation attributes:
        - customerid"""
        return self.execute("update_customer", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_customerbankaccount(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_customerbankaccount".
        
        Fields (from Docs samples):
        - accountholder
        - description
        
        Operation attributes:
        - recordno"""
        return self.execute("update_customerbankaccount", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_customerchargecard(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_customerchargecard".
        
        Fields (from Docs samples):
        - exp_month
        - exp_year
        
        Operation attributes:
        - recordno"""
        return self.execute("update_customerchargecard", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_department(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_department".
        
        Fields (from Docs samples):
        - title
        
        Operation attributes:
        - departmentid"""
        return self.execute("update_department", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_earningtype(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_earningtype".
        
        Fields (from Docs samples):
        - billableacctno
        - method
        - nonbillableacctno
        - ratemultiplier
        
        Operation attributes:
        - key"""
        return self.execute("update_earningtype", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_employee(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_employee".
        
        Fields (from Docs samples):
        - personalinfo.contactname
        - title
        
        Operation attributes:
        - employeeid"""
        return self.execute("update_employee", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_employeerate(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_employeerate".
        
        Fields (from Docs samples):
        - billingrate
        - ratestartdate.day
        - ratestartdate.month
        - ratestartdate.year
        - salaryrate
        
        Operation attributes:
        - key"""
        return self.execute("update_employeerate", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_expenseadjustmentreport(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_expenseadjustmentreport".
        
        Fields (from Docs samples):
        - updateexpenseadjustments.updateexpenseadjustment.expensetype
        
        Operation attributes:
        - key"""
        return self.execute("update_expenseadjustmentreport", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_expensepaymenttype(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_expensepaymenttype".
        
        Fields (from Docs samples):
        - offsetacctno
        
        Operation attributes:
        - name"""
        return self.execute("update_expensepaymenttype", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_expensereport(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_expensereport".
        
        Fields (from Docs samples):
        - description
        - updateexpenses.updateexpense.expensetype
        
        Operation attributes:
        - key"""
        return self.execute("update_expensereport", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_expensetype(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_expensetype".
        
        Fields (from Docs samples):
        - glaccountno
        
        Operation attributes:
        - expensetype"""
        return self.execute("update_expensetype", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_glaccount(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_glaccount".
        
        Fields (from Docs samples):
        - title
        
        Operation attributes:
        - glaccountno"""
        return self.execute("update_glaccount", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_ictransaction(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_ictransaction".
        
        Fields (from Docs samples):
        - updateictransitems.updateictransitem.itemdesc
        
        Operation attributes:
        - key"""
        return self.execute("update_ictransaction", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_invoice(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_invoice".
        
        Fields (from Docs samples):
        - updateinvoiceitems.updatelineitem.memo
        
        Operation attributes:
        - key"""
        return self.execute("update_invoice", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_item(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_item".
        
        Fields (from Docs samples):
        - name
        
        Operation attributes:
        - itemid"""
        return self.execute("update_item", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_location(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_location".
        
        Fields (from Docs samples):
        - name
        
        Operation attributes:
        - locationid"""
        return self.execute("update_location", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_otherreceipt(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_otherreceipt".
        
        Fields (from Docs samples):
        - receiptitems.lineitem.amount
        - receiptitems.lineitem.glaccountno
        - receiptitems.lineitem.locationid
        - receiptitems.updatelineitem.memo
        
        Operation attributes:
        - key"""
        return self.execute("update_otherreceipt", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_popricelist(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_popricelist".
        
        Fields (from Docs samples):
        - status
        
        Operation attributes:
        - name"""
        return self.execute("update_popricelist", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_potransaction(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_potransaction".
        
        Fields (from Docs samples):
        - updatepotransitems.updatepotransitem.memo
        
        Operation attributes:
        - key"""
        return self.execute("update_potransaction", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_revrecschedule(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_revrecschedule".
        
        Fields (from Docs samples):
        - memo
        - recordno
        - revrecentries.revrecentry.accountno
        - revrecentries.revrecentry.postingdate.day
        - revrecentries.revrecentry.postingdate.month
        - revrecentries.revrecentry.postingdate.year
        - revrecentries.revrecentry.recordno
        - revrecentries.revrecentry.trx_amount"""
        return self.execute("update_revrecschedule", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_savingsaccount(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_savingsaccount".
        
        Fields (from Docs samples):
        - phone
        
        Operation attributes:
        - bankaccountid"""
        return self.execute("update_savingsaccount", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_sopricelist(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_sopricelist".
        
        Fields (from Docs samples):
        - status
        
        Operation attributes:
        - name"""
        return self.execute("update_sopricelist", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_sotransaction(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_sotransaction".
        
        Fields (from Docs samples):
        - updatesotransitems.updatesotransitem.memo
        
        Operation attributes:
        - key"""
        return self.execute("update_sotransaction", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_statglaccount(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_statglaccount".
        
        Fields (from Docs samples):
        - title
        
        Operation attributes:
        - glaccountno"""
        return self.execute("update_statglaccount", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_supdoc(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_supdoc".
        
        Fields (from Docs samples):
        - attachments.attachment.attachmentdata
        - attachments.attachment.attachmentname
        - attachments.attachment.attachmenttype
        - supdocdescription
        - supdocfoldername
        - supdocid"""
        return self.execute("update_supdoc", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_supdocfolder(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_supdocfolder".
        
        Fields (from Docs samples):
        - supdocfolderdescription
        - supdocfoldername
        - supdocparentfoldername"""
        return self.execute("update_supdocfolder", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_task(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_task".
        
        Fields (from Docs samples):
        - projectid
        
        Operation attributes:
        - key"""
        return self.execute("update_task", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_territory(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_territory".
        
        Fields (from Docs samples):
        - managerid
        
        Operation attributes:
        - territoryid"""
        return self.execute("update_territory", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_timesheet(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_timesheet".
        
        Fields (from Docs samples):
        - begindate.day
        - begindate.month
        - begindate.year
        - employeeid
        - timesheetdescription
        - timesheetitems.timesheetitem.customerid
        - timesheetitems.timesheetitem.departmentid
        - timesheetitems.timesheetitem.entrydate.day
        - timesheetitems.timesheetitem.entrydate.month
        - timesheetitems.timesheetitem.entrydate.year
        - timesheetitems.timesheetitem.lineno
        - timesheetitems.timesheetitem.locationid
        - timesheetitems.timesheetitem.projectid
        - timesheetitems.timesheetitem.qty
        - timesheetitems.timesheetitem.taskname
        - timesheetitems.timesheetitem.timesheetentrydescription
        
        Operation attributes:
        - key"""
        return self.execute("update_timesheet", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_timetype(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_timetype".
        
        Fields (from Docs samples):
        - accountno
        
        Operation attributes:
        - key"""
        return self.execute("update_timetype", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def update_vendor(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "update_vendor".
        
        Fields (from Docs samples):
        - name
        - termname
        
        Operation attributes:
        - vendorid"""
        return self.execute("update_vendor", payload=payload, operation_attrs=operation_attrs, control_id=control_id)

    def void_appaymentrequest(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:
        """Execute "void_appaymentrequest".
        
        Fields (from Docs samples):
        - appaymentkeys.appaymentkey"""
        return self.execute("void_appaymentrequest", payload=payload, operation_attrs=operation_attrs, control_id=control_id)
