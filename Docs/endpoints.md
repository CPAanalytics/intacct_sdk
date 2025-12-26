# Endpoint Catalog

Status: todo | wip | done
Tests: unit | integration | fixture | live

| Operation | Object/Module | SDK Method | Status | Tests |
| --- | --- | --- | --- | --- |
| MY_ACH_OBJECT | ACHEFTFILE | OperationClient.my_ach_object | done | unit, fixture |
| apply_arpayment | Accounts Receivable | OperationClient.apply_arpayment | done | unit, fixture |
| approve | PODOCUMENT | OperationClient.approve | done | unit, fixture |
| approve | TIMESHEET | OperationClient.approve | done | unit, fixture |
| approveVendor | Accounts Payable | OperationClient.approve_vendor | done | unit, fixture |
| approve_appaymentrequest | Accounts Payable | OperationClient.approve_appaymentrequest | done | unit, fixture |
| cancel | JOBQUEUERECORD | OperationClient.cancel | done | unit, fixture |
| clearallmea | CONTRACT | OperationClient.clearallmea | done | unit, fixture |
| clearlastactivemea | CONTRACT | OperationClient.clearlastactivemea | done | unit, fixture |
| confirm_appaymentrequest | Accounts Payable | OperationClient.confirm_appaymentrequest | done | unit, fixture |
| consolidate | Consolidations | OperationClient.consolidate | done | unit, fixture |
| consolidatebytier | Consolidations | OperationClient.consolidatebytier | done | unit, fixture |
| create | ACCUMULATIONTYPE | SessionClient.create | done | unit, fixture |
| create | AFRSETUP | SessionClient.create | done | unit, fixture |
| create | ALLOCATION | SessionClient.create | done | unit, fixture |
| create | APACCOUNTLABEL | SessionClient.create | done | unit, fixture |
| create | APBILL | SessionClient.create | done | unit, fixture |
| create | APBILLJOINTPAYEE | SessionClient.create | done | unit, fixture |
| create | APPYMT | SessionClient.create | done | unit, fixture |
| create | APRETAINAGERELEASE | SessionClient.create | done | unit, fixture |
| create | ARACCOUNTLABEL | SessionClient.create | done | unit, fixture |
| create | ARADVANCE | SessionClient.create | done | unit, fixture |
| create | ARPYMT | SessionClient.create | done | unit, fixture |
| create | ARRETAINAGERELEASE | SessionClient.create | done | unit, fixture |
| create | BANKACCTRECON | SessionClient.create | done | unit, fixture |
| create | BANKACCTTXNFEED | SessionClient.create | done | unit, fixture |
| create | BIN | SessionClient.create | done | unit, fixture |
| create | BINFACE | SessionClient.create | done | unit, fixture |
| create | BINSIZE | SessionClient.create | done | unit, fixture |
| create | CHANGEREQUEST | SessionClient.create | done | unit, fixture |
| create | CHANGEREQUESTSTATUS | SessionClient.create | done | unit, fixture |
| create | CHANGEREQUESTTYPE | SessionClient.create | done | unit, fixture |
| create | CLASS | SessionClient.create | done | unit, fixture |
| create | COMPLIANCEDEFINITION | SessionClient.create | done | unit, fixture |
| create | COMPLIANCERECORD | SessionClient.create | done | unit, fixture |
| create | COMPLIANCETYPE | SessionClient.create | done | unit, fixture |
| create | CONTACT | SessionClient.create | done | unit, fixture |
| create | CONTRACT | SessionClient.create | done | unit, fixture |
| create | CONTRACTBILLINGTEMPLATE | SessionClient.create | done | unit, fixture |
| create | CONTRACTDETAIL | SessionClient.create | done | unit, fixture |
| create | CONTRACTEXPENSE | SessionClient.create | done | unit, fixture |
| create | CONTRACTEXPENSETEMPLATE | SessionClient.create | done | unit, fixture |
| create | CONTRACTITEMPRICELIST | SessionClient.create | done | unit, fixture |
| create | CONTRACTMEABUNDLE | SessionClient.create | done | unit, fixture |
| create | CONTRACTPRICELIST | SessionClient.create | done | unit, fixture |
| create | CONTRACTREVENUETEMPLATE | SessionClient.create | done | unit, fixture |
| create | CONTRACTTYPE | SessionClient.create | done | unit, fixture |
| create | CONTRACTUSAGE | SessionClient.create | done | unit, fixture |
| create | COSTTYPE | SessionClient.create | done | unit, fixture |
| create | CUSTOMER | SessionClient.create | done | unit, fixture |
| create | DEPARTMENT | SessionClient.create | done | unit, fixture |
| create | DUNNINGDEFINITION | SessionClient.create | done | unit, fixture |
| create | EEACCOUNTLABEL | SessionClient.create | done | unit, fixture |
| create | EMPLOYEE | SessionClient.create | done | unit, fixture |
| create | EMPLOYEEPOSITION | SessionClient.create | done | unit, fixture |
| create | EXCHANGERATE | SessionClient.create | done | unit, fixture |
| create | GCBOOK | SessionClient.create | done | unit, fixture |
| create | GCBOOKACCTRATETYPE | SessionClient.create | done | unit, fixture |
| create | GCBOOKADJJOURNAL | SessionClient.create | done | unit, fixture |
| create | GCBOOKELIMACCOUNT | SessionClient.create | done | unit, fixture |
| create | GCBOOKENTITY | SessionClient.create | done | unit, fixture |
| create | GCOWNERSHIPSTRUCTURE | SessionClient.create | done | unit, fixture |
| create | GCOWNERSHIPSTRUCTUREDETAIL | SessionClient.create | done | unit, fixture |
| create | GENINVOICEPOLICY | SessionClient.create | done | unit, fixture |
| create | GENINVOICEPREVIEW | SessionClient.create | done | unit, fixture |
| create | GENINVOICERUN | SessionClient.create | done | unit, fixture |
| create | GLACCOUNT | SessionClient.create | done | unit, fixture |
| create | GLACCTALLOCATION | SessionClient.create | done | unit, fixture |
| create | GLACCTALLOCATIONGRP | SessionClient.create | done | unit, fixture |
| create | GLACCTALLOCATIONRUN | SessionClient.create | done | unit, fixture |
| create | GLACCTGRP | SessionClient.create | done | unit, fixture |
| create | GLACCTGRPPURPOSE | SessionClient.create | done | unit, fixture |
| create | GLBATCH | SessionClient.create | done | unit, fixture |
| create | GLBUDGETHEADER | SessionClient.create | done | unit, fixture |
| create | ICCYCLECOUNT | SessionClient.create | done | unit, fixture |
| create | ICCYCLECOUNTENTRY | SessionClient.create | done | unit, fixture |
| create | ICTRANSFER | SessionClient.create | done | unit, fixture |
| create | ITEM | SessionClient.create | done | unit, fixture |
| create | ITEMCROSSREF | SessionClient.create | done | unit, fixture |
| create | LABORCLASS | SessionClient.create | done | unit, fixture |
| create | LABORSHIFT | SessionClient.create | done | unit, fixture |
| create | LABORUNION | SessionClient.create | done | unit, fixture |
| create | LOCATION | SessionClient.create | done | unit, fixture |
| create | OBSPCTCOMPLETED | SessionClient.create | done | unit, fixture |
| create | PAYROLLREPORTCHECK | SessionClient.create | done | unit, fixture |
| create | PAYROLLREPORTEMPLOYEE | SessionClient.create | done | unit, fixture |
| create | PAYROLLREPORTGROSSPAY | SessionClient.create | done | unit, fixture |
| create | PAYROLLREPORTPAYMODIFIER | SessionClient.create | done | unit, fixture |
| create | PAYROLLREPORTPTOACCRUALSCHEDULE | SessionClient.create | done | unit, fixture |
| create | PAYROLLREPORTPTOACTIVITY | SessionClient.create | done | unit, fixture |
| create | PAYROLLREPORTTAX | SessionClient.create | done | unit, fixture |
| create | PAYROLLREPORTTAXSETUP | SessionClient.create | done | unit, fixture |
| create | PAYROLLREPORTTIMECARD | SessionClient.create | done | unit, fixture |
| create | PAYROLLREPORTTRADE | SessionClient.create | done | unit, fixture |
| create | PJESTIMATE | SessionClient.create | done | unit, fixture |
| create | PJESTIMATEENTRY | SessionClient.create | done | unit, fixture |
| create | PJESTIMATETYPE | SessionClient.create | done | unit, fixture |
| create | PODOCUMENTPARAMS | SessionClient.create | done | unit, fixture |
| create | PROJECT | SessionClient.create | done | unit, fixture |
| create | PROJECTCHANGEORDER | SessionClient.create | done | unit, fixture |
| create | PROJECTCONTRACT | SessionClient.create | done | unit, fixture |
| create | PROJECTCONTRACTLINE | SessionClient.create | done | unit, fixture |
| create | PROJECTCONTRACTTYPE | SessionClient.create | done | unit, fixture |
| create | PROVIDERBANKACCOUNT | SessionClient.create | done | unit, fixture |
| create | PROVIDERVENDOR | SessionClient.create | done | unit, fixture |
| create | RATETABLE | SessionClient.create | done | unit, fixture |
| create | RECURGLACCTALLOCATION | SessionClient.create | done | unit, fixture |
| create | REPORTINGPERIOD | SessionClient.create | done | unit, fixture |
| create | STANDARDCOSTTYPE | SessionClient.create | done | unit, fixture |
| create | STANDARDTASK | SessionClient.create | done | unit, fixture |
| create | STATACCOUNT | SessionClient.create | done | unit, fixture |
| create | TASK | SessionClient.create | done | unit, fixture |
| create | TIMESHEET | SessionClient.create | done | unit, fixture |
| create | USERINFO | SessionClient.create | done | unit, fixture |
| create | USERROLES | SessionClient.create | done | unit, fixture |
| create | VENDOR | SessionClient.create | done | unit, fixture |
| create | WAREHOUSE | SessionClient.create | done | unit, fixture |
| create | ZONE | SessionClient.create | done | unit, fixture |
| create_achbankconfiguration | Cash Management | OperationClient.create_achbankconfiguration | done | unit, fixture |
| create_apaccountlabel | Accounts Payable | OperationClient.create_apaccountlabel | done | unit, fixture |
| create_apadjustment | Accounts Payable | OperationClient.create_apadjustment | done | unit, fixture |
| create_apadjustmentbatch | Accounts Payable | OperationClient.create_apadjustmentbatch | done | unit, fixture |
| create_appayment | Accounts Payable | OperationClient.create_appayment | done | unit, fixture |
| create_apterm | Accounts Payable | OperationClient.create_apterm | done | unit, fixture |
| create_araccountlabel | Accounts Receivable | OperationClient.create_araccountlabel | done | unit, fixture |
| create_aradjustment | Accounts Receivable | OperationClient.create_aradjustment | done | unit, fixture |
| create_aradjustmentbatch | Accounts Receivable | OperationClient.create_aradjustmentbatch | done | unit, fixture |
| create_arpayment | Accounts Receivable | OperationClient.create_arpayment | done | unit, fixture |
| create_arpaymentbatch | Accounts Receivable | OperationClient.create_arpaymentbatch | done | unit, fixture |
| create_arterm | Accounts Receivable | OperationClient.create_arterm | done | unit, fixture |
| create_bill | Accounts Payable | OperationClient.create_bill | done | unit, fixture |
| create_billbatch | Accounts Payable | OperationClient.create_billbatch | done | unit, fixture |
| create_class | Company and Console | OperationClient.create_class | done | unit, fixture |
| create_consolidation | Consolidations | OperationClient.create_consolidation | done | unit, fixture |
| create_contact | Company and Console | OperationClient.create_contact | done | unit, fixture |
| create_contacttaxgroup | Sales Tax VAT GST | OperationClient.create_contacttaxgroup | done | unit, fixture |
| create_customer | Accounts Receivable | OperationClient.create_customer | done | unit, fixture |
| create_customerbankaccount | Accounts Receivable | OperationClient.create_customerbankaccount | done | unit, fixture |
| create_customerchargecard | Accounts Receivable | OperationClient.create_customerchargecard | done | unit, fixture |
| create_department | Company and Console | OperationClient.create_department | done | unit, fixture |
| create_earningtype | Project Resource Management | OperationClient.create_earningtype | done | unit, fixture |
| create_employee | Employee Expenses | OperationClient.create_employee | done | unit, fixture |
| create_employeerate | Employee Expenses | OperationClient.create_employeerate | done | unit, fixture |
| create_expenseadjustmentreport | Employee Expenses | OperationClient.create_expenseadjustmentreport | done | unit, fixture |
| create_expensepaymenttype | Employee Expenses | OperationClient.create_expensepaymenttype | done | unit, fixture |
| create_expensereport | Employee Expenses | OperationClient.create_expensereport | done | unit, fixture |
| create_expensereportbatch | Employee Expenses | OperationClient.create_expensereportbatch | done | unit, fixture |
| create_expensetype | Employee Expenses | OperationClient.create_expensetype | done | unit, fixture |
| create_glaccount | General Ledger | OperationClient.create_glaccount | done | unit, fixture |
| create_gltransaction | General Ledger | OperationClient.create_gltransaction | done | unit, fixture |
| create_ictransaction | Inventory Control | OperationClient.create_ictransaction | done | unit, fixture |
| create_invoice | Accounts Receivable | OperationClient.create_invoice | done | unit, fixture |
| create_invoicebatch | Accounts Receivable | OperationClient.create_invoicebatch | done | unit, fixture |
| create_item | Inventory Control | OperationClient.create_item | done | unit, fixture |
| create_itemtaxgroup | Inventory Control | OperationClient.create_itemtaxgroup | done | unit, fixture |
| create_location | Company and Console | OperationClient.create_location | done | unit, fixture |
| create_paymentrequest | Accounts Payable | OperationClient.create_paymentrequest | done | unit, fixture |
| create_popricelist | Purchasing | OperationClient.create_popricelist | done | unit, fixture |
| create_potransaction | Purchasing | OperationClient.create_potransaction | done | unit, fixture |
| create_recurringbill | Accounts Payable | OperationClient.create_recurringbill | done | unit, fixture |
| create_recurringinvoice | Accounts Receivable | OperationClient.create_recurringinvoice | done | unit, fixture |
| create_recursotransaction | Order Entry | OperationClient.create_recursotransaction | done | unit, fixture |
| create_reimbursementrequest | Employee Expenses | OperationClient.create_reimbursementrequest | done | unit, fixture |
| create_savingsaccount | Cash Management | OperationClient.create_savingsaccount | done | unit, fixture |
| create_sopricelist | Order Entry | OperationClient.create_sopricelist | done | unit, fixture |
| create_sotransaction | Order Entry | OperationClient.create_sotransaction | done | unit, fixture |
| create_statglaccount | General Ledger | OperationClient.create_statglaccount | done | unit, fixture |
| create_statgltransaction | General Ledger | OperationClient.create_statgltransaction | done | unit, fixture |
| create_stkittransaction | Inventory Control | OperationClient.create_stkittransaction | done | unit, fixture |
| create_supdoc | Company and Console | OperationClient.create_supdoc | done | unit, fixture |
| create_supdocfolder | Company and Console | OperationClient.create_supdocfolder | done | unit, fixture |
| create_task | Project Resource Management | OperationClient.create_task | done | unit, fixture |
| create_territory | Accounts Receivable | OperationClient.create_territory | done | unit, fixture |
| create_timesheet | Project Resource Management | OperationClient.create_timesheet | done | unit, fixture |
| create_timetype | Project Resource Management | OperationClient.create_timetype | done | unit, fixture |
| create_vendor | Accounts Payable | OperationClient.create_vendor | done | unit, fixture |
| create_vendorentityaccountno | Accounts Payable | OperationClient.create_vendorentityaccountno | done | unit, fixture |
| decline | PODOCUMENT | OperationClient.decline | done | unit, fixture |
| decline | TIMESHEET | OperationClient.decline | done | unit, fixture |
| declineVendor | Accounts Payable | OperationClient.decline_vendor | done | unit, fixture |
| decline_appaymentrequest | Accounts Payable | OperationClient.decline_appaymentrequest | done | unit, fixture |
| delete | ACCUMULATIONTYPE | SessionClient.delete | done | unit, fixture |
| delete | ALLOCATION | SessionClient.delete | done | unit, fixture |
| delete | APACCOUNTLABEL | SessionClient.delete | done | unit, fixture |
| delete | APADJUSTMENT | SessionClient.delete | done | unit, fixture |
| delete | APBILL | SessionClient.delete | done | unit, fixture |
| delete | APBILLJOINTPAYEE | SessionClient.delete | done | unit, fixture |
| delete | APPYMT | SessionClient.delete | done | unit, fixture |
| delete | APRETAINAGERELEASE | SessionClient.delete | done | unit, fixture |
| delete | ARACCOUNTLABEL | SessionClient.delete | done | unit, fixture |
| delete | ARADJUSTMENT | SessionClient.delete | done | unit, fixture |
| delete | ARINVOICE | SessionClient.delete | done | unit, fixture |
| delete | ARPYMT | SessionClient.delete | done | unit, fixture |
| delete | ARRETAINAGERELEASE | SessionClient.delete | done | unit, fixture |
| delete | BANKACCTRECON | SessionClient.delete | done | unit, fixture |
| delete | BANKACCTTXNFEED | SessionClient.delete | done | unit, fixture |
| delete | BIN | SessionClient.delete | done | unit, fixture |
| delete | BINFACE | SessionClient.delete | done | unit, fixture |
| delete | BINSIZE | SessionClient.delete | done | unit, fixture |
| delete | CHANGEREQUEST | SessionClient.delete | done | unit, fixture |
| delete | CHANGEREQUESTENTRY | SessionClient.delete | done | unit, fixture |
| delete | CHANGEREQUESTSTATUS | SessionClient.delete | done | unit, fixture |
| delete | CHANGEREQUESTTYPE | SessionClient.delete | done | unit, fixture |
| delete | CLASS | SessionClient.delete | done | unit, fixture |
| delete | COGSCLOSEDJE | SessionClient.delete | done | unit, fixture |
| delete | COMPLIANCEDEFINITION | SessionClient.delete | done | unit, fixture |
| delete | COMPLIANCETYPE | SessionClient.delete | done | unit, fixture |
| delete | CONTACT | SessionClient.delete | done | unit, fixture |
| delete | CONTRACT | SessionClient.delete | done | unit, fixture |
| delete | CONTRACTBILLINGTEMPLATE | SessionClient.delete | done | unit, fixture |
| delete | CONTRACTDETAIL | SessionClient.delete | done | unit, fixture |
| delete | CONTRACTEXPENSE | SessionClient.delete | done | unit, fixture |
| delete | CONTRACTEXPENSETEMPLATE | SessionClient.delete | done | unit, fixture |
| delete | CONTRACTITEMPRICELIST | SessionClient.delete | done | unit, fixture |
| delete | CONTRACTPRICELIST | SessionClient.delete | done | unit, fixture |
| delete | CONTRACTREVENUETEMPLATE | SessionClient.delete | done | unit, fixture |
| delete | CONTRACTTYPE | SessionClient.delete | done | unit, fixture |
| delete | CONTRACTUSAGE | SessionClient.delete | done | unit, fixture |
| delete | COSTTYPE | SessionClient.delete | done | unit, fixture |
| delete | CUSTOMER | SessionClient.delete | done | unit, fixture |
| delete | DEPARTMENT | SessionClient.delete | done | unit, fixture |
| delete | DUNNINGDEFINITION | SessionClient.delete | done | unit, fixture |
| delete | EEACCOUNTLABEL | SessionClient.delete | done | unit, fixture |
| delete | EEXPENSES | SessionClient.delete | done | unit, fixture |
| delete | EMPLOYEE | SessionClient.delete | done | unit, fixture |
| delete | EMPLOYEEPOSITION | SessionClient.delete | done | unit, fixture |
| delete | ENTITYACCTDEFAULT | SessionClient.delete | done | unit, fixture |
| delete | ENTITYACCTOVERRIDE | SessionClient.delete | done | unit, fixture |
| delete | EXPENSEADJUSTMENTS | SessionClient.delete | done | unit, fixture |
| delete | GCBOOK | SessionClient.delete | done | unit, fixture |
| delete | GCBOOKACCTRATETYPE | SessionClient.delete | done | unit, fixture |
| delete | GCBOOKADJJOURNAL | SessionClient.delete | done | unit, fixture |
| delete | GCBOOKELIMACCOUNT | SessionClient.delete | done | unit, fixture |
| delete | GCBOOKENTITY | SessionClient.delete | done | unit, fixture |
| delete | GCOWNERSHIPCHILDENTITY | SessionClient.delete | done | unit, fixture |
| delete | GCOWNERSHIPENTITY | SessionClient.delete | done | unit, fixture |
| delete | GCOWNERSHIPSTRUCTURE | SessionClient.delete | done | unit, fixture |
| delete | GENINVOICEPOLICY | SessionClient.delete | done | unit, fixture |
| delete | GLACCOUNT | SessionClient.delete | done | unit, fixture |
| delete | GLACCTALLOCATION | SessionClient.delete | done | unit, fixture |
| delete | GLACCTALLOCATIONGRP | SessionClient.delete | done | unit, fixture |
| delete | GLACCTGRP | SessionClient.delete | done | unit, fixture |
| delete | GLACCTGRPPURPOSE | SessionClient.delete | done | unit, fixture |
| delete | GLBATCH | SessionClient.delete | done | unit, fixture |
| delete | GLBUDGETHEADER | SessionClient.delete | done | unit, fixture |
| delete | GLBUDGETITEM | SessionClient.delete | done | unit, fixture |
| delete | ICCYCLECOUNT | SessionClient.delete | done | unit, fixture |
| delete | ICCYCLECOUNTENTRY | SessionClient.delete | done | unit, fixture |
| delete | ICTRANSFER | SessionClient.delete | done | unit, fixture |
| delete | INVDOCUMENT | SessionClient.delete | done | unit, fixture |
| delete | ITEM | SessionClient.delete | done | unit, fixture |
| delete | ITEMCROSSREF | SessionClient.delete | done | unit, fixture |
| delete | LABORCLASS | SessionClient.delete | done | unit, fixture |
| delete | LABORSHIFT | SessionClient.delete | done | unit, fixture |
| delete | LABORUNION | SessionClient.delete | done | unit, fixture |
| delete | LOCATION | SessionClient.delete | done | unit, fixture |
| delete | OBSPCTCOMPLETED | SessionClient.delete | done | unit, fixture |
| delete | PAYROLLREPORTCHECK | SessionClient.delete | done | unit, fixture |
| delete | PAYROLLREPORTEMPLOYEE | SessionClient.delete | done | unit, fixture |
| delete | PAYROLLREPORTGROSSPAY | SessionClient.delete | done | unit, fixture |
| delete | PAYROLLREPORTPAYMODIFIER | SessionClient.delete | done | unit, fixture |
| delete | PAYROLLREPORTPTOACCRUALSCHEDULE | SessionClient.delete | done | unit, fixture |
| delete | PAYROLLREPORTPTOACTIVITY | SessionClient.delete | done | unit, fixture |
| delete | PAYROLLREPORTTAX | SessionClient.delete | done | unit, fixture |
| delete | PAYROLLREPORTTAXSETUP | SessionClient.delete | done | unit, fixture |
| delete | PAYROLLREPORTTIMECARD | SessionClient.delete | done | unit, fixture |
| delete | PAYROLLREPORTTRADE | SessionClient.delete | done | unit, fixture |
| delete | PJESTIMATE | SessionClient.delete | done | unit, fixture |
| delete | PJESTIMATEENTRY | SessionClient.delete | done | unit, fixture |
| delete | PJESTIMATETYPE | SessionClient.delete | done | unit, fixture |
| delete | PODOCUMENT | SessionClient.delete | done | unit, fixture |
| delete | PODOCUMENTPARAMS | SessionClient.delete | done | unit, fixture |
| delete | PROJECT | SessionClient.delete | done | unit, fixture |
| delete | PROJECTCHANGEORDER | SessionClient.delete | done | unit, fixture |
| delete | PROJECTCONTRACT | SessionClient.delete | done | unit, fixture |
| delete | PROJECTCONTRACTLINEENTRY | SessionClient.delete | done | unit, fixture |
| delete | PROJECTCONTRACTTYPE | SessionClient.delete | done | unit, fixture |
| delete | RATETABLE | SessionClient.delete | done | unit, fixture |
| delete | RECURGLACCTALLOCATION | SessionClient.delete | done | unit, fixture |
| delete | REPORTINGPERIOD | SessionClient.delete | done | unit, fixture |
| delete | STANDARDCOSTTYPE | SessionClient.delete | done | unit, fixture |
| delete | STANDARDTASK | SessionClient.delete | done | unit, fixture |
| delete | STATACCOUNT | SessionClient.delete | done | unit, fixture |
| delete | TASK | SessionClient.delete | done | unit, fixture |
| delete | TIMESHEET | SessionClient.delete | done | unit, fixture |
| delete | USERINFO | SessionClient.delete | done | unit, fixture |
| delete | VENDOR | SessionClient.delete | done | unit, fixture |
| delete | WAREHOUSE | SessionClient.delete | done | unit, fixture |
| delete | ZONE | SessionClient.delete | done | unit, fixture |
| delete | compliancerecord | SessionClient.delete | done | unit, fixture |
| delete_achbankconfiguration | Cash Management | OperationClient.delete_achbankconfiguration | done | unit, fixture |
| delete_apaccountlabel | Accounts Payable | OperationClient.delete_apaccountlabel | done | unit, fixture |
| delete_apadjustment | Accounts Payable | OperationClient.delete_apadjustment | done | unit, fixture |
| delete_apterm | Accounts Payable | OperationClient.delete_apterm | done | unit, fixture |
| delete_araccountlabel | Accounts Receivable | OperationClient.delete_araccountlabel | done | unit, fixture |
| delete_aradjustment | Accounts Receivable | OperationClient.delete_aradjustment | done | unit, fixture |
| delete_arterm | Accounts Receivable | OperationClient.delete_arterm | done | unit, fixture |
| delete_bill | Accounts Payable | OperationClient.delete_bill | done | unit, fixture |
| delete_class | Company and Console | OperationClient.delete_class | done | unit, fixture |
| delete_contact | Company and Console | OperationClient.delete_contact | done | unit, fixture |
| delete_contacttaxgroup | Sales Tax VAT GST | OperationClient.delete_contacttaxgroup | done | unit, fixture |
| delete_customer | Accounts Receivable | OperationClient.delete_customer | done | unit, fixture |
| delete_customerbankaccount | Accounts Receivable | OperationClient.delete_customerbankaccount | done | unit, fixture |
| delete_customerchargecard | Accounts Receivable | OperationClient.delete_customerchargecard | done | unit, fixture |
| delete_department | Company and Console | OperationClient.delete_department | done | unit, fixture |
| delete_earningtype | Project Resource Management | OperationClient.delete_earningtype | done | unit, fixture |
| delete_employee | Employee Expenses | OperationClient.delete_employee | done | unit, fixture |
| delete_employeerate | Employee Expenses | OperationClient.delete_employeerate | done | unit, fixture |
| delete_expenseadjustmentreport | Employee Expenses | OperationClient.delete_expenseadjustmentreport | done | unit, fixture |
| delete_expensepaymenttype | Employee Expenses | OperationClient.delete_expensepaymenttype | done | unit, fixture |
| delete_expensereport | Employee Expenses | OperationClient.delete_expensereport | done | unit, fixture |
| delete_expensetype | Employee Expenses | OperationClient.delete_expensetype | done | unit, fixture |
| delete_glaccount | General Ledger | OperationClient.delete_glaccount | done | unit, fixture |
| delete_gltransaction | General Ledger | OperationClient.delete_gltransaction | done | unit, fixture |
| delete_ictransaction | Inventory Control | OperationClient.delete_ictransaction | done | unit, fixture |
| delete_invoice | Accounts Receivable | OperationClient.delete_invoice | done | unit, fixture |
| delete_item | Inventory Control | OperationClient.delete_item | done | unit, fixture |
| delete_itemtaxgroup | Inventory Control | OperationClient.delete_itemtaxgroup | done | unit, fixture |
| delete_location | Company and Console | OperationClient.delete_location | done | unit, fixture |
| delete_otherreceipt | Cash Management | OperationClient.delete_otherreceipt | done | unit, fixture |
| delete_paymentrequest | Accounts Payable | OperationClient.delete_paymentrequest | done | unit, fixture |
| delete_popricelist | Purchasing | OperationClient.delete_popricelist | done | unit, fixture |
| delete_potransaction | Purchasing | OperationClient.delete_potransaction | done | unit, fixture |
| delete_recurringbill | Accounts Payable | OperationClient.delete_recurringbill | done | unit, fixture |
| delete_recurringinvoice | Accounts Receivable | OperationClient.delete_recurringinvoice | done | unit, fixture |
| delete_recursotransaction | Order Entry | OperationClient.delete_recursotransaction | done | unit, fixture |
| delete_savingsaccount | Cash Management | OperationClient.delete_savingsaccount | done | unit, fixture |
| delete_sopricelist | Order Entry | OperationClient.delete_sopricelist | done | unit, fixture |
| delete_sotransaction | Order Entry | OperationClient.delete_sotransaction | done | unit, fixture |
| delete_statglaccount | General Ledger | OperationClient.delete_statglaccount | done | unit, fixture |
| delete_supdoc | Company and Console | OperationClient.delete_supdoc | done | unit, fixture |
| delete_supdocfolder | Company and Console | OperationClient.delete_supdocfolder | done | unit, fixture |
| delete_task | Project Resource Management | OperationClient.delete_task | done | unit, fixture |
| delete_territory | Accounts Receivable | OperationClient.delete_territory | done | unit, fixture |
| delete_timesheet | Project Resource Management | OperationClient.delete_timesheet | done | unit, fixture |
| delete_timetype | Project Resource Management | OperationClient.delete_timetype | done | unit, fixture |
| delete_vendor | Accounts Payable | OperationClient.delete_vendor | done | unit, fixture |
| deliver | CONTRACTDETAIL | OperationClient.deliver | done | unit, fixture |
| get | Accounts Receivable | OperationClient.get | done | unit, fixture |
| get | Cash Management | OperationClient.get | done | unit, fixture |
| get | Company and Console | OperationClient.get | done | unit, fixture |
| getAPISession | Company and Console | IntacctClient.get_api_session | done | unit, fixture |
| getAPISession | Intacct API Authentication | IntacctClient.get_api_session | done | unit, fixture |
| getApprovalHistory | Purchasing | OperationClient.get_approval_history | done | unit, fixture |
| getAuditTrail | APBILL | OperationClient.get_audit_trail | done | unit, fixture |
| getDdsDdl | CUSTOMER | OperationClient.get_dds_ddl | done | unit, fixture |
| getDdsObjects | Data Delivery Service | OperationClient.get_dds_objects | done | unit, fixture |
| getDimensionAutofillDetails | Platform Services | OperationClient.get_dimension_autofill_details | done | unit, fixture |
| getDimensionRelationships | Platform Services | OperationClient.get_dimension_relationships | done | unit, fixture |
| getDimensionRestrictedData | Platform Services | OperationClient.get_dimension_restricted_data | done | unit, fixture |
| getDimensionRestrictions | Platform Services | OperationClient.get_dimension_restrictions | done | unit, fixture |
| getDimensions | Platform Services | OperationClient.get_dimensions | done | unit, fixture |
| getFinancialSetup | Company and Console | OperationClient.get_financial_setup | done | unit, fixture |
| getTransactionsToApprove | Purchasing | OperationClient.get_transactions_to_approve | done | unit, fixture |
| getUserPermissions | Company and Console | OperationClient.get_user_permissions | done | unit, fixture |
| getVendorApprovalHistory | Accounts Payable | OperationClient.get_vendor_approval_history | done | unit, fixture |
| getVendorsToApprove | Accounts Payable | OperationClient.get_vendors_to_approve | done | unit, fixture |
| get_accountbalances | General Ledger | OperationClient.get_accountbalances | done | unit, fixture |
| get_accountbalancesbydimensions | General Ledger | OperationClient.get_accountbalancesbydimensions | done | unit, fixture |
| get_applications | Company and Console | OperationClient.get_applications | done | unit, fixture |
| get_araging | Accounts Receivable | OperationClient.get_araging | done | unit, fixture |
| get_companyprefs | Company and Console | OperationClient.get_companyprefs | done | unit, fixture |
| get_list | Accounts Payable | OperationClient.get_list | done | unit, fixture |
| get_list | Accounts Receivable | OperationClient.get_list | done | unit, fixture |
| get_list | Cash Management | OperationClient.get_list | done | unit, fixture |
| get_list | Company and Console | OperationClient.get_list | done | unit, fixture |
| get_list | Customization Services | OperationClient.get_list | done | unit, fixture |
| get_list | Employee Expenses | OperationClient.get_list | done | unit, fixture |
| get_trialbalance | General Ledger | OperationClient.get_trialbalance | done | unit, fixture |
| hold | CONTRACTDETAIL | OperationClient.hold | done | unit, fixture |
| hold | CONTRACTEXPENSE | OperationClient.hold | done | unit, fixture |
| hold_revrecschedule | Order Entry | OperationClient.hold_revrecschedule | done | unit, fixture |
| inspect | * | OperationClient.inspect | done | unit, fixture |
| inspect | DEPARTMENT | OperationClient.inspect | done | unit, fixture |
| installApp | Platform Services | OperationClient.install_app | done | unit, fixture |
| lookup | ACCTTITLEBYLOC | OperationClient.lookup | done | unit, fixture |
| lookup | ACCUMULATIONTYPE | OperationClient.lookup | done | unit, fixture |
| lookup | ACHBANK | OperationClient.lookup | done | unit, fixture |
| lookup | ACTIVITYLOG | OperationClient.lookup | done | unit, fixture |
| lookup | ADVAUDITHISTORY | OperationClient.lookup | done | unit, fixture |
| lookup | AFRSETUP | OperationClient.lookup | done | unit, fixture |
| lookup | AISLE | OperationClient.lookup | done | unit, fixture |
| lookup | ALLOCATION | OperationClient.lookup | done | unit, fixture |
| lookup | ALLOCATIONENTRY | OperationClient.lookup | done | unit, fixture |
| lookup | APACCOUNTLABEL | OperationClient.lookup | done | unit, fixture |
| lookup | APADJUSTMENT | OperationClient.lookup | done | unit, fixture |
| lookup | APBILL | OperationClient.lookup | done | unit, fixture |
| lookup | APBILLBATCH | OperationClient.lookup | done | unit, fixture |
| lookup | APBILLITEM | OperationClient.lookup | done | unit, fixture |
| lookup | APBILLJOINTPAYEE | OperationClient.lookup | done | unit, fixture |
| lookup | APPAYMENTREQUEST | OperationClient.lookup | done | unit, fixture |
| lookup | APPYMT | OperationClient.lookup | done | unit, fixture |
| lookup | APPYMTDETAIL | OperationClient.lookup | done | unit, fixture |
| lookup | APRECURBILL | OperationClient.lookup | done | unit, fixture |
| lookup | APRECURBILLENTRY | OperationClient.lookup | done | unit, fixture |
| lookup | APRETAINAGERELEASE | OperationClient.lookup | done | unit, fixture |
| lookup | APRETAINAGERELEASEENTRY | OperationClient.lookup | done | unit, fixture |
| lookup | APTERM | OperationClient.lookup | done | unit, fixture |
| lookup | ARACCOUNTLABEL | OperationClient.lookup | done | unit, fixture |
| lookup | ARADJUSTMENT | OperationClient.lookup | done | unit, fixture |
| lookup | ARADJUSTMENTITEM | OperationClient.lookup | done | unit, fixture |
| lookup | ARADVANCE | OperationClient.lookup | done | unit, fixture |
| lookup | ARINVOICE | OperationClient.lookup | done | unit, fixture |
| lookup | ARINVOICEBATCH | OperationClient.lookup | done | unit, fixture |
| lookup | ARPYMT | OperationClient.lookup | done | unit, fixture |
| lookup | ARRECURINVOICE | OperationClient.lookup | done | unit, fixture |
| lookup | ARRECURINVOICEENTRY | OperationClient.lookup | done | unit, fixture |
| lookup | ARRETAINAGERELEASEENTRY | OperationClient.lookup | done | unit, fixture |
| lookup | ARTERM | OperationClient.lookup | done | unit, fixture |
| lookup | AUDITHISTORY | OperationClient.lookup | done | unit, fixture |
| lookup | AVAILABLEINVENTORY | OperationClient.lookup | done | unit, fixture |
| lookup | BANKACCTRECON | OperationClient.lookup | done | unit, fixture |
| lookup | BANKACCTTXNFEED | OperationClient.lookup | done | unit, fixture |
| lookup | BANKFEE | OperationClient.lookup | done | unit, fixture |
| lookup | BANKFEEENTRY | OperationClient.lookup | done | unit, fixture |
| lookup | BIN | OperationClient.lookup | done | unit, fixture |
| lookup | BINFACE | OperationClient.lookup | done | unit, fixture |
| lookup | BINSIZE | OperationClient.lookup | done | unit, fixture |
| lookup | CCTRANSACTION | OperationClient.lookup | done | unit, fixture |
| lookup | CCTRANSACTIONENTRY | OperationClient.lookup | done | unit, fixture |
| lookup | CHANGEREQUEST | OperationClient.lookup | done | unit, fixture |
| lookup | CHANGEREQUESTENTRY | OperationClient.lookup | done | unit, fixture |
| lookup | CHANGEREQUESTSTATUS | OperationClient.lookup | done | unit, fixture |
| lookup | CHANGEREQUESTTYPE | OperationClient.lookup | done | unit, fixture |
| lookup | CHARGEPAYOFF | OperationClient.lookup | done | unit, fixture |
| lookup | CHARGEPAYOFFENTRY | OperationClient.lookup | done | unit, fixture |
| lookup | CHECKINGACCOUNT | OperationClient.lookup | done | unit, fixture |
| lookup | CLASS | OperationClient.lookup | done | unit, fixture |
| lookup | CLASSGROUP | OperationClient.lookup | done | unit, fixture |
| lookup | COGSCLOSEDJE | OperationClient.lookup | done | unit, fixture |
| lookup | COMPLIANCEDEFINITION | OperationClient.lookup | done | unit, fixture |
| lookup | COMPLIANCERECORD | OperationClient.lookup | done | unit, fixture |
| lookup | COMPLIANCETYPE | OperationClient.lookup | done | unit, fixture |
| lookup | CONTACT | OperationClient.lookup | done | unit, fixture |
| lookup | CONTRACT | OperationClient.lookup | done | unit, fixture |
| lookup | CONTRACTBILLINGSCHEDULE | OperationClient.lookup | done | unit, fixture |
| lookup | CONTRACTBILLINGSCHEDULEENTRY | OperationClient.lookup | done | unit, fixture |
| lookup | CONTRACTBILLINGTEMPLATE | OperationClient.lookup | done | unit, fixture |
| lookup | CONTRACTBILLINGTEMPLATEENTRY | OperationClient.lookup | done | unit, fixture |
| lookup | CONTRACTDETAIL | OperationClient.lookup | done | unit, fixture |
| lookup | CONTRACTEXPENSE | OperationClient.lookup | done | unit, fixture |
| lookup | CONTRACTEXPENSE2SCHEDULE | OperationClient.lookup | done | unit, fixture |
| lookup | CONTRACTEXPENSESCHEDULE | OperationClient.lookup | done | unit, fixture |
| lookup | CONTRACTEXPENSETEMPLATE | OperationClient.lookup | done | unit, fixture |
| lookup | CONTRACTGROUP | OperationClient.lookup | done | unit, fixture |
| lookup | CONTRACTITEMPRCLSTENTYTIER | OperationClient.lookup | done | unit, fixture |
| lookup | CONTRACTITEMPRICELIST | OperationClient.lookup | done | unit, fixture |
| lookup | CONTRACTITEMPRICELISTENTRY | OperationClient.lookup | done | unit, fixture |
| lookup | CONTRACTMEABUNDLE | OperationClient.lookup | done | unit, fixture |
| lookup | CONTRACTMEAITEMPRICELIST | OperationClient.lookup | done | unit, fixture |
| lookup | CONTRACTMEAITEMPRICELISTENTRY | OperationClient.lookup | done | unit, fixture |
| lookup | CONTRACTMEAPRICELIST | OperationClient.lookup | done | unit, fixture |
| lookup | CONTRACTPRICELIST | OperationClient.lookup | done | unit, fixture |
| lookup | CONTRACTREVENUE2SCHEDULE | OperationClient.lookup | done | unit, fixture |
| lookup | CONTRACTREVENUESCHEDULE | OperationClient.lookup | done | unit, fixture |
| lookup | CONTRACTREVENUETEMPLATE | OperationClient.lookup | done | unit, fixture |
| lookup | CONTRACTTYPE | OperationClient.lookup | done | unit, fixture |
| lookup | CONTRACTUSAGE | OperationClient.lookup | done | unit, fixture |
| lookup | COSTTYPE | OperationClient.lookup | done | unit, fixture |
| lookup | CREDITCARD | OperationClient.lookup | done | unit, fixture |
| lookup | CREDITCARDFEE | OperationClient.lookup | done | unit, fixture |
| lookup | CREDITCARDFEEENTRY | OperationClient.lookup | done | unit, fixture |
| lookup | CUSTOMER | OperationClient.lookup | done | unit, fixture |
| lookup | CUSTOMEREMAILTEMPLATE | OperationClient.lookup | done | unit, fixture |
| lookup | CUSTOMERGROUP | OperationClient.lookup | done | unit, fixture |
| lookup | CUSTOMERVISIBILITY | OperationClient.lookup | done | unit, fixture |
| lookup | CUSTTYPE | OperationClient.lookup | done | unit, fixture |
| lookup | DDSJOB | OperationClient.lookup | done | unit, fixture |
| lookup | DEPARTMENT | OperationClient.lookup | done | unit, fixture |
| lookup | DEPARTMENTGROUP | OperationClient.lookup | done | unit, fixture |
| lookup | DEPOSIT | OperationClient.lookup | done | unit, fixture |
| lookup | DEPOSITENTRY | OperationClient.lookup | done | unit, fixture |
| lookup | DUNNINGDEFINITION | OperationClient.lookup | done | unit, fixture |
| lookup | EARNINGTYPE | OperationClient.lookup | done | unit, fixture |
| lookup | EEACCOUNTLABEL | OperationClient.lookup | done | unit, fixture |
| lookup | EEXPENSES | OperationClient.lookup | done | unit, fixture |
| lookup | EMPLOYEE | OperationClient.lookup | done | unit, fixture |
| lookup | EMPLOYEEGROUP | OperationClient.lookup | done | unit, fixture |
| lookup | EMPLOYEEPOSITION | OperationClient.lookup | done | unit, fixture |
| lookup | EMPLOYEETYPE | OperationClient.lookup | done | unit, fixture |
| lookup | EPPAYMENT | OperationClient.lookup | done | unit, fixture |
| lookup | EPPAYMENTREQUEST | OperationClient.lookup | done | unit, fixture |
| lookup | EXCHANGERATE | OperationClient.lookup | done | unit, fixture |
| lookup | EXCHANGERATEENTRY | OperationClient.lookup | done | unit, fixture |
| lookup | EXCHANGERATETYPES | OperationClient.lookup | done | unit, fixture |
| lookup | EXPENSEADJUSTMENTS | OperationClient.lookup | done | unit, fixture |
| lookup | EXPENSEADJUSTMENTSITEM | OperationClient.lookup | done | unit, fixture |
| lookup | EXPENSEPAYMENTTYPE | OperationClient.lookup | done | unit, fixture |
| lookup | FUNDSTRANSFER | OperationClient.lookup | done | unit, fixture |
| lookup | GCBOOK | OperationClient.lookup | done | unit, fixture |
| lookup | GCBOOKACCTRATETYPE | OperationClient.lookup | done | unit, fixture |
| lookup | GCBOOKADJJOURNAL | OperationClient.lookup | done | unit, fixture |
| lookup | GCBOOKELIMACCOUNT | OperationClient.lookup | done | unit, fixture |
| lookup | GCBOOKENTITY | OperationClient.lookup | done | unit, fixture |
| lookup | GCOWNERSHIPCHILDENTITY | OperationClient.lookup | done | unit, fixture |
| lookup | GCOWNERSHIPENTITY | OperationClient.lookup | done | unit, fixture |
| lookup | GCOWNERSHIPSTRUCTURE | OperationClient.lookup | done | unit, fixture |
| lookup | GCOWNERSHIPSTRUCTUREDETAIL | OperationClient.lookup | done | unit, fixture |
| lookup | GENINVOICEPOLICY | OperationClient.lookup | done | unit, fixture |
| lookup | GENINVOICEPREVIEW | OperationClient.lookup | done | unit, fixture |
| lookup | GENINVOICEPREVIEWLINE | OperationClient.lookup | done | unit, fixture |
| lookup | GENINVOICERUN | OperationClient.lookup | done | unit, fixture |
| lookup | GLACCOUNT | OperationClient.lookup | done | unit, fixture |
| lookup | GLACCOUNTBALANCE | OperationClient.lookup | done | unit, fixture |
| lookup | GLACCTALLOCATION | OperationClient.lookup | done | unit, fixture |
| lookup | GLACCTALLOCATIONGRP | OperationClient.lookup | done | unit, fixture |
| lookup | GLACCTALLOCATIONRUN | OperationClient.lookup | done | unit, fixture |
| lookup | GLACCTGRP | OperationClient.lookup | done | unit, fixture |
| lookup | GLACCTGRPHIERARCHY | OperationClient.lookup | done | unit, fixture |
| lookup | GLACCTGRPPURPOSE | OperationClient.lookup | done | unit, fixture |
| lookup | GLBATCH | OperationClient.lookup | done | unit, fixture |
| lookup | GLBUDGETHEADER | OperationClient.lookup | done | unit, fixture |
| lookup | GLBUDGETITEM | OperationClient.lookup | done | unit, fixture |
| lookup | GLDETAIL | OperationClient.lookup | done | unit, fixture |
| lookup | GLENTRY | OperationClient.lookup | done | unit, fixture |
| lookup | ICCYCLECOUNT | OperationClient.lookup | done | unit, fixture |
| lookup | ICCYCLECOUNTENTRY | OperationClient.lookup | done | unit, fixture |
| lookup | ICROW | OperationClient.lookup | done | unit, fixture |
| lookup | ICTRANSFERITEM | OperationClient.lookup | done | unit, fixture |
| lookup | INVDOCUMENT | OperationClient.lookup | done | unit, fixture |
| lookup | INVDOCUMENTENTRY | OperationClient.lookup | done | unit, fixture |
| lookup | INVDOCUMENTPARAMS | OperationClient.lookup | done | unit, fixture |
| lookup | INVDOCUMENTSUBTOTALS | OperationClient.lookup | done | unit, fixture |
| lookup | INVENTORYTOTALDETAIL | OperationClient.lookup | done | unit, fixture |
| lookup | INVPRICELIST | OperationClient.lookup | done | unit, fixture |
| lookup | ITEM | OperationClient.lookup | done | unit, fixture |
| lookup | ITEMCROSSREF | OperationClient.lookup | done | unit, fixture |
| lookup | ITEMGLGROUP | OperationClient.lookup | done | unit, fixture |
| lookup | ITEMGROUP | OperationClient.lookup | done | unit, fixture |
| lookup | ITEMTAXGROUP | OperationClient.lookup | done | unit, fixture |
| lookup | ITEMWAREHOUSEINFO | OperationClient.lookup | done | unit, fixture |
| lookup | InventoryWQDetail | OperationClient.lookup | done | unit, fixture |
| lookup | InventoryWQOrder | OperationClient.lookup | done | unit, fixture |
| lookup | JOBQUEUERECORD | OperationClient.lookup | done | unit, fixture |
| lookup | LABORCLASS | OperationClient.lookup | done | unit, fixture |
| lookup | LABORSHIFT | OperationClient.lookup | done | unit, fixture |
| lookup | LABORUNION | OperationClient.lookup | done | unit, fixture |
| lookup | LOCATION | OperationClient.lookup | done | unit, fixture |
| lookup | LOCATIONENTITY | OperationClient.lookup | done | unit, fixture |
| lookup | LOCATIONGROUP | OperationClient.lookup | done | unit, fixture |
| lookup | MCA_attendee | OperationClient.lookup | done | unit, fixture |
| lookup | MEMBERUSERGROUP | OperationClient.lookup | done | unit, fixture |
| lookup | OBSPCTCOMPLETED | OperationClient.lookup | done | unit, fixture |
| lookup | OTHERRECEIPTS | OperationClient.lookup | done | unit, fixture |
| lookup | OTHERRECEIPTSENTRY | OperationClient.lookup | done | unit, fixture |
| lookup | PAYROLLREPORTCHECK | OperationClient.lookup | done | unit, fixture |
| lookup | PAYROLLREPORTEMPLOYEE | OperationClient.lookup | done | unit, fixture |
| lookup | PAYROLLREPORTGROSSPAY | OperationClient.lookup | done | unit, fixture |
| lookup | PAYROLLREPORTPAYMODIFIER | OperationClient.lookup | done | unit, fixture |
| lookup | PAYROLLREPORTPTOACCRUALSCHEDULE | OperationClient.lookup | done | unit, fixture |
| lookup | PAYROLLREPORTPTOACTIVITY | OperationClient.lookup | done | unit, fixture |
| lookup | PAYROLLREPORTTAX | OperationClient.lookup | done | unit, fixture |
| lookup | PAYROLLREPORTTAXSETUP | OperationClient.lookup | done | unit, fixture |
| lookup | PAYROLLREPORTTIMECARD | OperationClient.lookup | done | unit, fixture |
| lookup | PAYROLLREPORTTRADE | OperationClient.lookup | done | unit, fixture |
| lookup | PJESTIMATE | OperationClient.lookup | done | unit, fixture |
| lookup | PJESTIMATEENTRY | OperationClient.lookup | done | unit, fixture |
| lookup | PJESTIMATETYPE | OperationClient.lookup | done | unit, fixture |
| lookup | PODOCUMENT | OperationClient.lookup | done | unit, fixture |
| lookup | PODOCUMENTENTRY | OperationClient.lookup | done | unit, fixture |
| lookup | PODOCUMENTPARAMS | OperationClient.lookup | done | unit, fixture |
| lookup | PODOCUMENTSUBTOTALS | OperationClient.lookup | done | unit, fixture |
| lookup | POPRICELIST | OperationClient.lookup | done | unit, fixture |
| lookup | POSITIONSKILL | OperationClient.lookup | done | unit, fixture |
| lookup | POSUBTOTALTEMPLATE | OperationClient.lookup | done | unit, fixture |
| lookup | PRODUCTLINE | OperationClient.lookup | done | unit, fixture |
| lookup | PROJECT | OperationClient.lookup | done | unit, fixture |
| lookup | PROJECTCHANGEORDER | OperationClient.lookup | done | unit, fixture |
| lookup | PROJECTCONTRACT | OperationClient.lookup | done | unit, fixture |
| lookup | PROJECTCONTRACTLINE | OperationClient.lookup | done | unit, fixture |
| lookup | PROJECTCONTRACTLINEENTRY | OperationClient.lookup | done | unit, fixture |
| lookup | PROJECTCONTRACTTYPE | OperationClient.lookup | done | unit, fixture |
| lookup | PROJECTGROUP | OperationClient.lookup | done | unit, fixture |
| lookup | PROJECTRESOURCES | OperationClient.lookup | done | unit, fixture |
| lookup | PROJECTSTATUS | OperationClient.lookup | done | unit, fixture |
| lookup | PROJECTTYPE | OperationClient.lookup | done | unit, fixture |
| lookup | PROVIDERBANKACCOUNT | OperationClient.lookup | done | unit, fixture |
| lookup | PROVIDERPAYMENTMETHOD | OperationClient.lookup | done | unit, fixture |
| lookup | PROVIDERVENDOR | OperationClient.lookup | done | unit, fixture |
| lookup | PTAPPLICATION | OperationClient.lookup | done | unit, fixture |
| lookup | RATETABLE | OperationClient.lookup | done | unit, fixture |
| lookup | RATETABLEAPENTRY | OperationClient.lookup | done | unit, fixture |
| lookup | RECURGLACCTALLOCATION | OperationClient.lookup | done | unit, fixture |
| lookup | REPORTINGPERIOD | OperationClient.lookup | done | unit, fixture |
| lookup | REVRECSCHEDULE | OperationClient.lookup | done | unit, fixture |
| lookup | REVRECSCHEDULEENTRY | OperationClient.lookup | done | unit, fixture |
| lookup | ROLEASSIGNMENT | OperationClient.lookup | done | unit, fixture |
| lookup | ROLEGROUPS | OperationClient.lookup | done | unit, fixture |
| lookup | ROLEPOLICYASSIGNMENT | OperationClient.lookup | done | unit, fixture |
| lookup | ROLES | OperationClient.lookup | done | unit, fixture |
| lookup | ROLEUSERS | OperationClient.lookup | done | unit, fixture |
| lookup | SAVINGSACCOUNT | OperationClient.lookup | done | unit, fixture |
| lookup | SODOCUMENT | OperationClient.lookup | done | unit, fixture |
| lookup | SODOCUMENTENTRY | OperationClient.lookup | done | unit, fixture |
| lookup | SODOCUMENTPARAMS | OperationClient.lookup | done | unit, fixture |
| lookup | SODOCUMENTSUBTOTALS | OperationClient.lookup | done | unit, fixture |
| lookup | SOPRICELIST | OperationClient.lookup | done | unit, fixture |
| lookup | SORECURDOCUMENT | OperationClient.lookup | done | unit, fixture |
| lookup | SOSUBTOTALTEMPLATE | OperationClient.lookup | done | unit, fixture |
| lookup | STANDARDCOSTTYPE | OperationClient.lookup | done | unit, fixture |
| lookup | STANDARDTASK | OperationClient.lookup | done | unit, fixture |
| lookup | STATACCOUNT | OperationClient.lookup | done | unit, fixture |
| lookup | TASK | OperationClient.lookup | done | unit, fixture |
| lookup | TASKRESOURCES | OperationClient.lookup | done | unit, fixture |
| lookup | TAXDETAIL | OperationClient.lookup | done | unit, fixture |
| lookup | TAXRECORD | OperationClient.lookup | done | unit, fixture |
| lookup | TAXSOLUTION | OperationClient.lookup | done | unit, fixture |
| lookup | TIMESHEET | OperationClient.lookup | done | unit, fixture |
| lookup | TIMETYPE | OperationClient.lookup | done | unit, fixture |
| lookup | TRANSACTIONRULE | OperationClient.lookup | done | unit, fixture |
| lookup | UOM | OperationClient.lookup | done | unit, fixture |
| lookup | UOMDETAIL | OperationClient.lookup | done | unit, fixture |
| lookup | USERGROUP | OperationClient.lookup | done | unit, fixture |
| lookup | USERINFO | OperationClient.lookup | done | unit, fixture |
| lookup | USERRESTRICTION | OperationClient.lookup | done | unit, fixture |
| lookup | USERRIGHTS | OperationClient.lookup | done | unit, fixture |
| lookup | USERROLES | OperationClient.lookup | done | unit, fixture |
| lookup | VENDOR | OperationClient.lookup | done | unit, fixture |
| lookup | VENDOREMAILTEMPLATE | OperationClient.lookup | done | unit, fixture |
| lookup | VENDORGROUP | OperationClient.lookup | done | unit, fixture |
| lookup | VENDORVISIBILITY | OperationClient.lookup | done | unit, fixture |
| lookup | VENDTYPE | OperationClient.lookup | done | unit, fixture |
| lookup | WAREHOUSE | OperationClient.lookup | done | unit, fixture |
| lookup | WAREHOUSEGROUP | OperationClient.lookup | done | unit, fixture |
| lookup | ZONE | OperationClient.lookup | done | unit, fixture |
| partialupdate_potransaction | Purchasing | OperationClient.partialupdate_potransaction | done | unit, fixture |
| post | CONTRACT | OperationClient.post | done | unit, fixture |
| post | CONTRACTDETAIL | OperationClient.post | done | unit, fixture |
| post | CONTRACTEXPENSE | OperationClient.post | done | unit, fixture |
| post | CONTRACTEXPENSE2SCHEDULE | OperationClient.post | done | unit, fixture |
| post | CONTRACTEXPENSESCHEDULE | OperationClient.post | done | unit, fixture |
| post | CONTRACTEXPENSESCHEDULEENTRY | OperationClient.post | done | unit, fixture |
| post | CONTRACTREVENUE2SCHEDULE | OperationClient.post | done | unit, fixture |
| post | CONTRACTREVENUESCHEDULE | OperationClient.post | done | unit, fixture |
| post | CONTRACTREVENUESCHEDULEENTRY | OperationClient.post | done | unit, fixture |
| post_revrecscheduleentry | Order Entry | OperationClient.post_revrecscheduleentry | done | unit, fixture |
| promote | JOBQUEUERECORD | OperationClient.promote | done | unit, fixture |
| query | ACCTTITLEBYLOC | OperationClient.query | done | unit, fixture |
| query | ACCUMULATIONTYPE | OperationClient.query | done | unit, fixture |
| query | ACHBANK | OperationClient.query | done | unit, fixture |
| query | ACTIVITYLOG | OperationClient.query | done | unit, fixture |
| query | ADVAUDITHISTORY | OperationClient.query | done | unit, fixture |
| query | AISLE | OperationClient.query | done | unit, fixture |
| query | ALLOCATION | OperationClient.query | done | unit, fixture |
| query | ALLOCATIONENTRY | OperationClient.query | done | unit, fixture |
| query | APACCOUNTLABEL | OperationClient.query | done | unit, fixture |
| query | APADJUSTMENT | OperationClient.query | done | unit, fixture |
| query | APBILL | OperationClient.query | done | unit, fixture |
| query | APBILLBATCH | OperationClient.query | done | unit, fixture |
| query | APBILLITEM | OperationClient.query | done | unit, fixture |
| query | APBILLJOINTPAYEE | OperationClient.query | done | unit, fixture |
| query | APPAYMENTREQUEST | OperationClient.query | done | unit, fixture |
| query | APPYMT | OperationClient.query | done | unit, fixture |
| query | APPYMTDETAIL | OperationClient.query | done | unit, fixture |
| query | APRECURBILL | OperationClient.query | done | unit, fixture |
| query | APRECURBILLENTRY | OperationClient.query | done | unit, fixture |
| query | APRETAINAGERELEASE | OperationClient.query | done | unit, fixture |
| query | APRETAINAGERELEASEENTRY | OperationClient.query | done | unit, fixture |
| query | APTERM | OperationClient.query | done | unit, fixture |
| query | ARACCOUNTLABEL | OperationClient.query | done | unit, fixture |
| query | ARADJUSTMENT | OperationClient.query | done | unit, fixture |
| query | ARADJUSTMENTITEM | OperationClient.query | done | unit, fixture |
| query | ARADVANCE | OperationClient.query | done | unit, fixture |
| query | ARINVOICE | OperationClient.query | done | unit, fixture |
| query | ARINVOICEBATCH | OperationClient.query | done | unit, fixture |
| query | ARINVOICEITEM | OperationClient.query | done | unit, fixture |
| query | ARPYMT | OperationClient.query | done | unit, fixture |
| query | ARRECURINVOICE | OperationClient.query | done | unit, fixture |
| query | ARRECURINVOICEENTRY | OperationClient.query | done | unit, fixture |
| query | ARRETAINAGERELEASE | OperationClient.query | done | unit, fixture |
| query | ARRETAINAGERELEASEENTRY | OperationClient.query | done | unit, fixture |
| query | ARTERM | OperationClient.query | done | unit, fixture |
| query | AUDITHISTORY | OperationClient.query | done | unit, fixture |
| query | AVAILABLEINVENTORY | OperationClient.query | done | unit, fixture |
| query | BANKACCTRECON | OperationClient.query | done | unit, fixture |
| query | BANKACCTTXNFEED | OperationClient.query | done | unit, fixture |
| query | BANKFEE | OperationClient.query | done | unit, fixture |
| query | BANKFEEENTRY | OperationClient.query | done | unit, fixture |
| query | BIN | OperationClient.query | done | unit, fixture |
| query | BINFACE | OperationClient.query | done | unit, fixture |
| query | BINSIZE | OperationClient.query | done | unit, fixture |
| query | CCTRANSACTION | OperationClient.query | done | unit, fixture |
| query | CCTRANSACTIONENTRY | OperationClient.query | done | unit, fixture |
| query | CHANGEREQUEST | OperationClient.query | done | unit, fixture |
| query | CHANGEREQUESTENTRY | OperationClient.query | done | unit, fixture |
| query | CHANGEREQUESTSTATUS | OperationClient.query | done | unit, fixture |
| query | CHANGEREQUESTTYPE | OperationClient.query | done | unit, fixture |
| query | CHARGEPAYOFF | OperationClient.query | done | unit, fixture |
| query | CHARGEPAYOFFENTRY | OperationClient.query | done | unit, fixture |
| query | CHECKINGACCOUNT | OperationClient.query | done | unit, fixture |
| query | CLASS | OperationClient.query | done | unit, fixture |
| query | CLASSGROUP | OperationClient.query | done | unit, fixture |
| query | COGSCLOSEDJE | OperationClient.query | done | unit, fixture |
| query | COMPLIANCEDEFINITION | OperationClient.query | done | unit, fixture |
| query | COMPLIANCERECORD | OperationClient.query | done | unit, fixture |
| query | COMPLIANCETYPE | OperationClient.query | done | unit, fixture |
| query | CONTACT | OperationClient.query | done | unit, fixture |
| query | CONTRACT | OperationClient.query | done | unit, fixture |
| query | CONTRACTBILLINGSCHEDULE | OperationClient.query | done | unit, fixture |
| query | CONTRACTBILLINGSCHEDULEENTRY | OperationClient.query | done | unit, fixture |
| query | CONTRACTBILLINGTEMPLATE | OperationClient.query | done | unit, fixture |
| query | CONTRACTBILLINGTEMPLATEENTRY | OperationClient.query | done | unit, fixture |
| query | CONTRACTDETAIL | OperationClient.query | done | unit, fixture |
| query | CONTRACTEXPENSE | OperationClient.query | done | unit, fixture |
| query | CONTRACTEXPENSE2SCHEDULE | OperationClient.query | done | unit, fixture |
| query | CONTRACTEXPENSESCHEDULE | OperationClient.query | done | unit, fixture |
| query | CONTRACTEXPENSETEMPLATE | OperationClient.query | done | unit, fixture |
| query | CONTRACTGROUP | OperationClient.query | done | unit, fixture |
| query | CONTRACTITEMPRCLSTENTYTIER | OperationClient.query | done | unit, fixture |
| query | CONTRACTITEMPRICELIST | OperationClient.query | done | unit, fixture |
| query | CONTRACTITEMPRICELISTENTRY | OperationClient.query | done | unit, fixture |
| query | CONTRACTMEABUNDLE | OperationClient.query | done | unit, fixture |
| query | CONTRACTMEAITEMPRICELIST | OperationClient.query | done | unit, fixture |
| query | CONTRACTMEAITEMPRICELISTENTRY | OperationClient.query | done | unit, fixture |
| query | CONTRACTMEAPRICELIST | OperationClient.query | done | unit, fixture |
| query | CONTRACTPRICELIST | OperationClient.query | done | unit, fixture |
| query | CONTRACTREVENUE2SCHEDULE | OperationClient.query | done | unit, fixture |
| query | CONTRACTREVENUESCHEDULE | OperationClient.query | done | unit, fixture |
| query | CONTRACTREVENUETEMPLATE | OperationClient.query | done | unit, fixture |
| query | CONTRACTTYPE | OperationClient.query | done | unit, fixture |
| query | CONTRACTUSAGE | OperationClient.query | done | unit, fixture |
| query | COSTTYPE | OperationClient.query | done | unit, fixture |
| query | CREDITCARD | OperationClient.query | done | unit, fixture |
| query | CREDITCARDFEE | OperationClient.query | done | unit, fixture |
| query | CREDITCARDFEEENTRY | OperationClient.query | done | unit, fixture |
| query | CUSTOMER | OperationClient.query | done | unit, fixture |
| query | CUSTOMEREMAILTEMPLATE | OperationClient.query | done | unit, fixture |
| query | CUSTOMERGROUP | OperationClient.query | done | unit, fixture |
| query | CUSTTYPE | OperationClient.query | done | unit, fixture |
| query | DDSJOB | OperationClient.query | done | unit, fixture |
| query | DEPARTMENT | OperationClient.query | done | unit, fixture |
| query | DEPARTMENTGROUP | OperationClient.query | done | unit, fixture |
| query | DEPOSIT | OperationClient.query | done | unit, fixture |
| query | DEPOSITENTRY | OperationClient.query | done | unit, fixture |
| query | EARNINGTYPE | OperationClient.query | done | unit, fixture |
| query | EEACCOUNTLABEL | OperationClient.query | done | unit, fixture |
| query | EEXPENSES | OperationClient.query | done | unit, fixture |
| query | EMPLOYEE | OperationClient.query | done | unit, fixture |
| query | EMPLOYEEGROUP | OperationClient.query | done | unit, fixture |
| query | EMPLOYEEPOSITION | OperationClient.query | done | unit, fixture |
| query | EPPAYMENT | OperationClient.query | done | unit, fixture |
| query | EPPAYMENTREQUEST | OperationClient.query | done | unit, fixture |
| query | EXCHANGERATE | OperationClient.query | done | unit, fixture |
| query | EXCHANGERATEENTRY | OperationClient.query | done | unit, fixture |
| query | EXCHANGERATETYPES | OperationClient.query | done | unit, fixture |
| query | EXPENSEADJUSTMENTS | OperationClient.query | done | unit, fixture |
| query | EXPENSEADJUSTMENTSITEM | OperationClient.query | done | unit, fixture |
| query | EXPENSEPAYMENTTYPE | OperationClient.query | done | unit, fixture |
| query | FUNDSTRANSFER | OperationClient.query | done | unit, fixture |
| query | FUNDSTRANSFERENTRY | OperationClient.query | done | unit, fixture |
| query | GCBOOK | OperationClient.query | done | unit, fixture |
| query | GCBOOKACCTRATETYPE | OperationClient.query | done | unit, fixture |
| query | GCBOOKADJJOURNAL | OperationClient.query | done | unit, fixture |
| query | GCBOOKELIMACCOUNT | OperationClient.query | done | unit, fixture |
| query | GCBOOKENTITY | OperationClient.query | done | unit, fixture |
| query | GCOWNERSHIPCHILDENTITY | OperationClient.query | done | unit, fixture |
| query | GCOWNERSHIPENTITY | OperationClient.query | done | unit, fixture |
| query | GCOWNERSHIPSTRUCTURE | OperationClient.query | done | unit, fixture |
| query | GCOWNERSHIPSTRUCTUREDETAIL | OperationClient.query | done | unit, fixture |
| query | GENINVOICEPOLICY | OperationClient.query | done | unit, fixture |
| query | GENINVOICEPREVIEW | OperationClient.query | done | unit, fixture |
| query | GENINVOICEPREVIEWLINE | OperationClient.query | done | unit, fixture |
| query | GENINVOICERUN | OperationClient.query | done | unit, fixture |
| query | GLACCOUNT | OperationClient.query | done | unit, fixture |
| query | GLACCTALLOCATION | OperationClient.query | done | unit, fixture |
| query | GLACCTALLOCATIONGRP | OperationClient.query | done | unit, fixture |
| query | GLACCTALLOCATIONRUN | OperationClient.query | done | unit, fixture |
| query | GLACCTGRP | OperationClient.query | done | unit, fixture |
| query | GLACCTGRPHIERARCHY | OperationClient.query | done | unit, fixture |
| query | GLACCTGRPPURPOSE | OperationClient.query | done | unit, fixture |
| query | GLBATCH | OperationClient.query | done | unit, fixture |
| query | GLBUDGETHEADER | OperationClient.query | done | unit, fixture |
| query | GLBUDGETITEM | OperationClient.query | done | unit, fixture |
| query | GLDETAIL | OperationClient.query | done | unit, fixture |
| query | GLENTRY | OperationClient.query | done | unit, fixture |
| query | ICCYCLECOUNT | OperationClient.query | done | unit, fixture |
| query | ICCYCLECOUNTENTRY | OperationClient.query | done | unit, fixture |
| query | ICROW | OperationClient.query | done | unit, fixture |
| query | ICTRANSFER | OperationClient.query | done | unit, fixture |
| query | INVDOCUMENT | OperationClient.query | done | unit, fixture |
| query | INVDOCUMENTENTRY | OperationClient.query | done | unit, fixture |
| query | INVDOCUMENTPARAMS | OperationClient.query | done | unit, fixture |
| query | INVDOCUMENTSUBTOTALS | OperationClient.query | done | unit, fixture |
| query | INVENTORYTOTALDETAIL | OperationClient.query | done | unit, fixture |
| query | INVPRICELIST | OperationClient.query | done | unit, fixture |
| query | ITEM | OperationClient.query | done | unit, fixture |
| query | ITEMCROSSREF | OperationClient.query | done | unit, fixture |
| query | ITEMGLGROUP | OperationClient.query | done | unit, fixture |
| query | ITEMGROUP | OperationClient.query | done | unit, fixture |
| query | ITEMTAXGROUP | OperationClient.query | done | unit, fixture |
| query | ITEMWAREHOUSEINFO | OperationClient.query | done | unit, fixture |
| query | InventoryWQDetail | OperationClient.query | done | unit, fixture |
| query | InventoryWQOrder | OperationClient.query | done | unit, fixture |
| query | JOBQUEUERECORD | OperationClient.query | done | unit, fixture |
| query | LABORCLASS | OperationClient.query | done | unit, fixture |
| query | LABORSHIFT | OperationClient.query | done | unit, fixture |
| query | LABORUNION | OperationClient.query | done | unit, fixture |
| query | LOCATIONENTITY | OperationClient.query | done | unit, fixture |
| query | LOCATIONGROUP | OperationClient.query | done | unit, fixture |
| query | MEMBERUSERGROUP | OperationClient.query | done | unit, fixture |
| query | OBSPCTCOMPLETED | OperationClient.query | done | unit, fixture |
| query | OTHERRECEIPTS | OperationClient.query | done | unit, fixture |
| query | OTHERRECEIPTSENTRY | OperationClient.query | done | unit, fixture |
| query | PAYROLLREPORTCHECK | OperationClient.query | done | unit, fixture |
| query | PAYROLLREPORTEMPLOYEE | OperationClient.query | done | unit, fixture |
| query | PAYROLLREPORTGROSSPAY | OperationClient.query | done | unit, fixture |
| query | PAYROLLREPORTPAYMODIFIER | OperationClient.query | done | unit, fixture |
| query | PAYROLLREPORTPTOACCRUALSCHEDULE | OperationClient.query | done | unit, fixture |
| query | PAYROLLREPORTPTOACTIVITY | OperationClient.query | done | unit, fixture |
| query | PAYROLLREPORTTAX | OperationClient.query | done | unit, fixture |
| query | PAYROLLREPORTTAXSETUP | OperationClient.query | done | unit, fixture |
| query | PAYROLLREPORTTIMECARD | OperationClient.query | done | unit, fixture |
| query | PAYROLLREPORTTRADE | OperationClient.query | done | unit, fixture |
| query | PJESTIMATE | OperationClient.query | done | unit, fixture |
| query | PJESTIMATEENTRY | OperationClient.query | done | unit, fixture |
| query | PJESTIMATETYPE | OperationClient.query | done | unit, fixture |
| query | PODOCUMENT | OperationClient.query | done | unit, fixture |
| query | PODOCUMENTENTRY | OperationClient.query | done | unit, fixture |
| query | PODOCUMENTPARAMS | OperationClient.query | done | unit, fixture |
| query | PODOCUMENTSUBTOTALS | OperationClient.query | done | unit, fixture |
| query | POPRICELIST | OperationClient.query | done | unit, fixture |
| query | POSITIONSKILL | OperationClient.query | done | unit, fixture |
| query | PRODUCTLINE | OperationClient.query | done | unit, fixture |
| query | PROJECT | OperationClient.query | done | unit, fixture |
| query | PROJECTCHANGEORDER | OperationClient.query | done | unit, fixture |
| query | PROJECTCONTRACT | OperationClient.query | done | unit, fixture |
| query | PROJECTCONTRACTLINE | OperationClient.query | done | unit, fixture |
| query | PROJECTCONTRACTLINEENTRY | OperationClient.query | done | unit, fixture |
| query | PROJECTCONTRACTTYPE | OperationClient.query | done | unit, fixture |
| query | PROJECTGROUP | OperationClient.query | done | unit, fixture |
| query | PROJECTRESOURCES | OperationClient.query | done | unit, fixture |
| query | PROJECTSTATUS | OperationClient.query | done | unit, fixture |
| query | PROJECTTYPE | OperationClient.query | done | unit, fixture |
| query | PROVIDERBANKACCOUNT | OperationClient.query | done | unit, fixture |
| query | PROVIDERPAYMENTMETHOD | OperationClient.query | done | unit, fixture |
| query | PROVIDERVENDOR | OperationClient.query | done | unit, fixture |
| query | PTAPPLICATION | OperationClient.query | done | unit, fixture |
| query | RATETABLE | OperationClient.query | done | unit, fixture |
| query | RATETABLEAPENTRY | OperationClient.query | done | unit, fixture |
| query | RATETABLEPOENTRY | OperationClient.query | done | unit, fixture |
| query | RATETABLETSENTRY | OperationClient.query | done | unit, fixture |
| query | RECURGLACCTALLOCATION | OperationClient.query | done | unit, fixture |
| query | REPORTINGPERIOD | OperationClient.query | done | unit, fixture |
| query | ROLEASSIGNMENT | OperationClient.query | done | unit, fixture |
| query | ROLEGROUPS | OperationClient.query | done | unit, fixture |
| query | ROLEPOLICYASSIGNMENT | OperationClient.query | done | unit, fixture |
| query | ROLES | OperationClient.query | done | unit, fixture |
| query | ROLEUSERS | OperationClient.query | done | unit, fixture |
| query | SAVINGSACCOUNT | OperationClient.query | done | unit, fixture |
| query | SODOCUMENT | OperationClient.query | done | unit, fixture |
| query | SODOCUMENTENTRY | OperationClient.query | done | unit, fixture |
| query | SODOCUMENTPARAMS | OperationClient.query | done | unit, fixture |
| query | SODOCUMENTSUBTOTALS | OperationClient.query | done | unit, fixture |
| query | SOPRICELIST | OperationClient.query | done | unit, fixture |
| query | SORECURDOCUMENT | OperationClient.query | done | unit, fixture |
| query | SOSUBTOTALTEMPLATE | OperationClient.query | done | unit, fixture |
| query | STANDARDCOSTTYPE | OperationClient.query | done | unit, fixture |
| query | STANDARDTASK | OperationClient.query | done | unit, fixture |
| query | STATACCOUNT | OperationClient.query | done | unit, fixture |
| query | TASK | OperationClient.query | done | unit, fixture |
| query | TASKRESOURCES | OperationClient.query | done | unit, fixture |
| query | TAXDETAIL | OperationClient.query | done | unit, fixture |
| query | TAXRECORD | OperationClient.query | done | unit, fixture |
| query | TAXSOLUTION | OperationClient.query | done | unit, fixture |
| query | TIMESHEET | OperationClient.query | done | unit, fixture |
| query | TIMESHEETAPPROVAL | OperationClient.query | done | unit, fixture |
| query | TIMESHEETENTRY | OperationClient.query | done | unit, fixture |
| query | TIMETYPE | OperationClient.query | done | unit, fixture |
| query | TRANSACTIONRULE | OperationClient.query | done | unit, fixture |
| query | UOM | OperationClient.query | done | unit, fixture |
| query | UOMDETAIL | OperationClient.query | done | unit, fixture |
| query | USERGROUP | OperationClient.query | done | unit, fixture |
| query | USERINFO | OperationClient.query | done | unit, fixture |
| query | USERRESTRICTION | OperationClient.query | done | unit, fixture |
| query | USERRIGHTS | OperationClient.query | done | unit, fixture |
| query | USERROLES | OperationClient.query | done | unit, fixture |
| query | VENDOR | OperationClient.query | done | unit, fixture |
| query | VENDOREMAILTEMPLATE | OperationClient.query | done | unit, fixture |
| query | VENDORGROUP | OperationClient.query | done | unit, fixture |
| query | VENDTYPE | OperationClient.query | done | unit, fixture |
| query | WAREHOUSE | OperationClient.query | done | unit, fixture |
| query | WAREHOUSEGROUP | OperationClient.query | done | unit, fixture |
| query | ZONE | OperationClient.query | done | unit, fixture |
| read | ACCTTITLEBYLOC | SessionClient.read | done | unit, fixture |
| read | ACCUMULATIONTYPE | SessionClient.read | done | unit, fixture |
| read | ACHBANK | SessionClient.read | done | unit, fixture |
| read | ACTIVITYLOG | SessionClient.read | done | unit, fixture |
| read | AFRSETUP | SessionClient.read | done | unit, fixture |
| read | AISLE | SessionClient.read | done | unit, fixture |
| read | ALLOCATION | SessionClient.read | done | unit, fixture |
| read | ALLOCATIONENTRY | SessionClient.read | done | unit, fixture |
| read | APACCOUNTLABEL | SessionClient.read | done | unit, fixture |
| read | APADJUSTMENT | SessionClient.read | done | unit, fixture |
| read | APBILL | SessionClient.read | done | unit, fixture |
| read | APBILLBATCH | SessionClient.read | done | unit, fixture |
| read | APBILLITEM | SessionClient.read | done | unit, fixture |
| read | APBILLJOINTPAYEE | SessionClient.read | done | unit, fixture |
| read | APPAYMENT | SessionClient.read | done | unit, fixture |
| read | APPAYMENTREQUEST | SessionClient.read | done | unit, fixture |
| read | APPYMT | SessionClient.read | done | unit, fixture |
| read | APPYMTDETAIL | SessionClient.read | done | unit, fixture |
| read | APRECURBILL | SessionClient.read | done | unit, fixture |
| read | APRECURBILLENTRY | SessionClient.read | done | unit, fixture |
| read | APRETAINAGERELEASE | SessionClient.read | done | unit, fixture |
| read | APRETAINAGERELEASEENTRY | SessionClient.read | done | unit, fixture |
| read | APTERM | SessionClient.read | done | unit, fixture |
| read | ARACCOUNTLABEL | SessionClient.read | done | unit, fixture |
| read | ARADJUSTMENT | SessionClient.read | done | unit, fixture |
| read | ARADVANCE | SessionClient.read | done | unit, fixture |
| read | ARINVOICE | SessionClient.read | done | unit, fixture |
| read | ARINVOICEBATCH | SessionClient.read | done | unit, fixture |
| read | ARPAYMENT | SessionClient.read | done | unit, fixture |
| read | ARPYMT | SessionClient.read | done | unit, fixture |
| read | ARRECURINVOICE | SessionClient.read | done | unit, fixture |
| read | ARRETAINAGERELEASE | SessionClient.read | done | unit, fixture |
| read | ARRETAINAGERELEASEENTRY | SessionClient.read | done | unit, fixture |
| read | ARTERM | SessionClient.read | done | unit, fixture |
| read | AVAILABLEINVENTORY | SessionClient.read | done | unit, fixture |
| read | BANKACCTRECON | SessionClient.read | done | unit, fixture |
| read | BANKACCTTXNFEED | SessionClient.read | done | unit, fixture |
| read | BANKFEE | SessionClient.read | done | unit, fixture |
| read | BANKFEEENTRY | SessionClient.read | done | unit, fixture |
| read | BIN | SessionClient.read | done | unit, fixture |
| read | BINFACE | SessionClient.read | done | unit, fixture |
| read | BINSIZE | SessionClient.read | done | unit, fixture |
| read | CCTRANSACTION | SessionClient.read | done | unit, fixture |
| read | CCTRANSACTIONENTRY | SessionClient.read | done | unit, fixture |
| read | CHANGEREQUEST | SessionClient.read | done | unit, fixture |
| read | CHANGEREQUESTENTRY | SessionClient.read | done | unit, fixture |
| read | CHANGEREQUESTSTATUS | SessionClient.read | done | unit, fixture |
| read | CHANGEREQUESTTYPE | SessionClient.read | done | unit, fixture |
| read | CHARGEPAYOFF | SessionClient.read | done | unit, fixture |
| read | CHARGEPAYOFFENTRY | SessionClient.read | done | unit, fixture |
| read | CHECKINGACCOUNT | SessionClient.read | done | unit, fixture |
| read | CLASS | SessionClient.read | done | unit, fixture |
| read | CLASSGROUP | SessionClient.read | done | unit, fixture |
| read | COGSCLOSEDJE | SessionClient.read | done | unit, fixture |
| read | COMPLIANCEDEFINITION | SessionClient.read | done | unit, fixture |
| read | COMPLIANCERECORD | SessionClient.read | done | unit, fixture |
| read | COMPLIANCETYPE | SessionClient.read | done | unit, fixture |
| read | CONTACT | SessionClient.read | done | unit, fixture |
| read | CONTRACT | SessionClient.read | done | unit, fixture |
| read | CONTRACTBILLINGSCHEDULE | SessionClient.read | done | unit, fixture |
| read | CONTRACTBILLINGSCHEDULEENTRY | SessionClient.read | done | unit, fixture |
| read | CONTRACTBILLINGTEMPLATE | SessionClient.read | done | unit, fixture |
| read | CONTRACTBILLINGTEMPLATEENTRY | SessionClient.read | done | unit, fixture |
| read | CONTRACTDETAIL | SessionClient.read | done | unit, fixture |
| read | CONTRACTEXPENSE | SessionClient.read | done | unit, fixture |
| read | CONTRACTEXPENSE2SCHEDULE | SessionClient.read | done | unit, fixture |
| read | CONTRACTEXPENSESCHEDULE | SessionClient.read | done | unit, fixture |
| read | CONTRACTEXPENSETEMPLATE | SessionClient.read | done | unit, fixture |
| read | CONTRACTGROUP | SessionClient.read | done | unit, fixture |
| read | CONTRACTITEMPRCLSTENTYTIER | SessionClient.read | done | unit, fixture |
| read | CONTRACTITEMPRICELIST | SessionClient.read | done | unit, fixture |
| read | CONTRACTITEMPRICELISTENTRY | SessionClient.read | done | unit, fixture |
| read | CONTRACTMEABUNDLE | SessionClient.read | done | unit, fixture |
| read | CONTRACTMEAITEMPRICELIST | SessionClient.read | done | unit, fixture |
| read | CONTRACTMEAITEMPRICELISTENTRY | SessionClient.read | done | unit, fixture |
| read | CONTRACTMEAPRICELIST | SessionClient.read | done | unit, fixture |
| read | CONTRACTPRICELIST | SessionClient.read | done | unit, fixture |
| read | CONTRACTREVENUE2SCHEDULE | SessionClient.read | done | unit, fixture |
| read | CONTRACTREVENUESCHEDULE | SessionClient.read | done | unit, fixture |
| read | CONTRACTREVENUETEMPLATE | SessionClient.read | done | unit, fixture |
| read | CONTRACTTYPE | SessionClient.read | done | unit, fixture |
| read | CONTRACTUSAGE | SessionClient.read | done | unit, fixture |
| read | COSTTYPE | SessionClient.read | done | unit, fixture |
| read | CREDITCARD | SessionClient.read | done | unit, fixture |
| read | CREDITCARDFEE | SessionClient.read | done | unit, fixture |
| read | CREDITCARDFEEENTRY | SessionClient.read | done | unit, fixture |
| read | CUSTOMER | SessionClient.read | done | unit, fixture |
| read | CUSTOMEREMAILTEMPLATE | SessionClient.read | done | unit, fixture |
| read | CUSTOMERGROUP | SessionClient.read | done | unit, fixture |
| read | CUSTOMERVISIBILITY | SessionClient.read | done | unit, fixture |
| read | CUSTTYPE | SessionClient.read | done | unit, fixture |
| read | DDSJOB | SessionClient.read | done | unit, fixture |
| read | DEPARTMENT | SessionClient.read | done | unit, fixture |
| read | DEPARTMENTGROUP | SessionClient.read | done | unit, fixture |
| read | DEPOSIT | SessionClient.read | done | unit, fixture |
| read | DEPOSITENTRY | SessionClient.read | done | unit, fixture |
| read | DUNNINGDEFINITION | SessionClient.read | done | unit, fixture |
| read | EARNINGTYPE | SessionClient.read | done | unit, fixture |
| read | EEACCOUNTLABEL | SessionClient.read | done | unit, fixture |
| read | EEXPENSES | SessionClient.read | done | unit, fixture |
| read | EMPLOYEE | SessionClient.read | done | unit, fixture |
| read | EMPLOYEEGROUP | SessionClient.read | done | unit, fixture |
| read | EMPLOYEEPOSITION | SessionClient.read | done | unit, fixture |
| read | EMPLOYEETYPE | SessionClient.read | done | unit, fixture |
| read | EPPAYMENT | SessionClient.read | done | unit, fixture |
| read | EPPAYMENTREQUEST | SessionClient.read | done | unit, fixture |
| read | EXCHANGERATE | SessionClient.read | done | unit, fixture |
| read | EXCHANGERATEENTRY | SessionClient.read | done | unit, fixture |
| read | EXCHANGERATETYPES | SessionClient.read | done | unit, fixture |
| read | EXPENSEADJUSTMENTS | SessionClient.read | done | unit, fixture |
| read | EXPENSEADJUSTMENTSITEM | SessionClient.read | done | unit, fixture |
| read | EXPENSEPAYMENTTYPE | SessionClient.read | done | unit, fixture |
| read | FUNDSTRANSFER | SessionClient.read | done | unit, fixture |
| read | GCBOOK | SessionClient.read | done | unit, fixture |
| read | GCBOOKACCTRATETYPE | SessionClient.read | done | unit, fixture |
| read | GCBOOKADJJOURNAL | SessionClient.read | done | unit, fixture |
| read | GCBOOKELIMACCOUNT | SessionClient.read | done | unit, fixture |
| read | GCBOOKENTITY | SessionClient.read | done | unit, fixture |
| read | GCOWNERSHIPCHILDENTITY | SessionClient.read | done | unit, fixture |
| read | GCOWNERSHIPENTITY | SessionClient.read | done | unit, fixture |
| read | GCOWNERSHIPSTRUCTURE | SessionClient.read | done | unit, fixture |
| read | GCOWNERSHIPSTRUCTUREDETAIL | SessionClient.read | done | unit, fixture |
| read | GENINVOICEPOLICY | SessionClient.read | done | unit, fixture |
| read | GENINVOICEPREVIEW | SessionClient.read | done | unit, fixture |
| read | GENINVOICEPREVIEWLINE | SessionClient.read | done | unit, fixture |
| read | GENINVOICERUN | SessionClient.read | done | unit, fixture |
| read | GLACCOUNT | SessionClient.read | done | unit, fixture |
| read | GLACCTALLOCATION | SessionClient.read | done | unit, fixture |
| read | GLACCTALLOCATIONGRP | SessionClient.read | done | unit, fixture |
| read | GLACCTALLOCATIONRUN | SessionClient.read | done | unit, fixture |
| read | GLACCTGRP | SessionClient.read | done | unit, fixture |
| read | GLACCTGRPPURPOSE | SessionClient.read | done | unit, fixture |
| read | GLBATCH | SessionClient.read | done | unit, fixture |
| read | GLBUDGETHEADER | SessionClient.read | done | unit, fixture |
| read | GLBUDGETITEM | SessionClient.read | done | unit, fixture |
| read | GLENTRY | SessionClient.read | done | unit, fixture |
| read | ICCYCLECOUNT | SessionClient.read | done | unit, fixture |
| read | ICCYCLECOUNTENTRY | SessionClient.read | done | unit, fixture |
| read | ICROW | SessionClient.read | done | unit, fixture |
| read | ICTRANSFER | SessionClient.read | done | unit, fixture |
| read | INTERENTITYSETUP | SessionClient.read | done | unit, fixture |
| read | INVDOCUMENT | SessionClient.read | done | unit, fixture |
| read | INVDOCUMENTENTRY | SessionClient.read | done | unit, fixture |
| read | INVDOCUMENTPARAMS | SessionClient.read | done | unit, fixture |
| read | INVDOCUMENTSUBTOTALS | SessionClient.read | done | unit, fixture |
| read | INVENTORYTOTALDETAIL | SessionClient.read | done | unit, fixture |
| read | INVPRICELIST | SessionClient.read | done | unit, fixture |
| read | ITEM | SessionClient.read | done | unit, fixture |
| read | ITEMCROSSREF | SessionClient.read | done | unit, fixture |
| read | ITEMGLGROUP | SessionClient.read | done | unit, fixture |
| read | ITEMGROUP | SessionClient.read | done | unit, fixture |
| read | ITEMTAXGROUP | SessionClient.read | done | unit, fixture |
| read | ITEMWAREHOUSEINFO | SessionClient.read | done | unit, fixture |
| read | InventoryWQDetail | SessionClient.read | done | unit, fixture |
| read | InventoryWQOrder | SessionClient.read | done | unit, fixture |
| read | JOBQUEUERECORD | SessionClient.read | done | unit, fixture |
| read | LABORCLASS | SessionClient.read | done | unit, fixture |
| read | LABORSHIFT | SessionClient.read | done | unit, fixture |
| read | LABORUNION | SessionClient.read | done | unit, fixture |
| read | LOCATION | SessionClient.read | done | unit, fixture |
| read | LOCATIONENTITY | SessionClient.read | done | unit, fixture |
| read | LOCATIONGROUP | SessionClient.read | done | unit, fixture |
| read | MEMBERUSERGROUP | SessionClient.read | done | unit, fixture |
| read | OBSPCTCOMPLETED | SessionClient.read | done | unit, fixture |
| read | OTHERRECEIPTS | SessionClient.read | done | unit, fixture |
| read | OTHERRECEIPTSENTRY | SessionClient.read | done | unit, fixture |
| read | PAYROLLREPORTCHECK | SessionClient.read | done | unit, fixture |
| read | PAYROLLREPORTEMPLOYEE | SessionClient.read | done | unit, fixture |
| read | PAYROLLREPORTGROSSPAY | SessionClient.read | done | unit, fixture |
| read | PAYROLLREPORTPAYMODIFIER | SessionClient.read | done | unit, fixture |
| read | PAYROLLREPORTPTOACCRUALSCHEDULE | SessionClient.read | done | unit, fixture |
| read | PAYROLLREPORTPTOACTIVITY | SessionClient.read | done | unit, fixture |
| read | PAYROLLREPORTTAX | SessionClient.read | done | unit, fixture |
| read | PAYROLLREPORTTAXSETUP | SessionClient.read | done | unit, fixture |
| read | PAYROLLREPORTTIMECARD | SessionClient.read | done | unit, fixture |
| read | PAYROLLREPORTTRADE | SessionClient.read | done | unit, fixture |
| read | PJESTIMATE | SessionClient.read | done | unit, fixture |
| read | PJESTIMATEENTRY | SessionClient.read | done | unit, fixture |
| read | PJESTIMATETYPE | SessionClient.read | done | unit, fixture |
| read | PODOCUMENT | SessionClient.read | done | unit, fixture |
| read | PODOCUMENTENTRY | SessionClient.read | done | unit, fixture |
| read | PODOCUMENTPARAMS | SessionClient.read | done | unit, fixture |
| read | PODOCUMENTSUBTOTALS | SessionClient.read | done | unit, fixture |
| read | POPRICELIST | SessionClient.read | done | unit, fixture |
| read | POSITIONSKILL | SessionClient.read | done | unit, fixture |
| read | POSUBTOTALTEMPLATE | SessionClient.read | done | unit, fixture |
| read | PRODUCTLINE | SessionClient.read | done | unit, fixture |
| read | PROJECT | SessionClient.read | done | unit, fixture |
| read | PROJECTCHANGEORDER | SessionClient.read | done | unit, fixture |
| read | PROJECTCONTRACT | SessionClient.read | done | unit, fixture |
| read | PROJECTCONTRACTLINE | SessionClient.read | done | unit, fixture |
| read | PROJECTCONTRACTLINEENTRY | SessionClient.read | done | unit, fixture |
| read | PROJECTCONTRACTTYPE | SessionClient.read | done | unit, fixture |
| read | PROJECTGROUP | SessionClient.read | done | unit, fixture |
| read | PROJECTRESOURCES | SessionClient.read | done | unit, fixture |
| read | PROJECTSTATUS | SessionClient.read | done | unit, fixture |
| read | PROJECTTYPE | SessionClient.read | done | unit, fixture |
| read | PROVIDERBANKACCOUNT | SessionClient.read | done | unit, fixture |
| read | PROVIDERPAYMENTMETHOD | SessionClient.read | done | unit, fixture |
| read | PROVIDERVENDOR | SessionClient.read | done | unit, fixture |
| read | PTAPPLICATION | SessionClient.read | done | unit, fixture |
| read | RATETABLE | SessionClient.read | done | unit, fixture |
| read | RATETABLEAPENTRY | SessionClient.read | done | unit, fixture |
| read | RATETABLEPOENTRY | SessionClient.read | done | unit, fixture |
| read | RATETABLETSENTRY | SessionClient.read | done | unit, fixture |
| read | RECURGLACCTALLOCATION | SessionClient.read | done | unit, fixture |
| read | REPORTINGPERIOD | SessionClient.read | done | unit, fixture |
| read | REVRECSCHEDULE | SessionClient.read | done | unit, fixture |
| read | REVRECSCHEDULEENTRY | SessionClient.read | done | unit, fixture |
| read | ROLEASSIGNMENT | SessionClient.read | done | unit, fixture |
| read | ROLEGROUPS | SessionClient.read | done | unit, fixture |
| read | ROLEPOLICYASSIGNMENT | SessionClient.read | done | unit, fixture |
| read | ROLES | SessionClient.read | done | unit, fixture |
| read | ROLEUSERS | SessionClient.read | done | unit, fixture |
| read | SAVINGSACCOUNT | SessionClient.read | done | unit, fixture |
| read | SODOCUMENT | SessionClient.read | done | unit, fixture |
| read | SODOCUMENTENTRY | SessionClient.read | done | unit, fixture |
| read | SODOCUMENTPARAMS | SessionClient.read | done | unit, fixture |
| read | SODOCUMENTSUBTOTALS | SessionClient.read | done | unit, fixture |
| read | SOPRICELIST | SessionClient.read | done | unit, fixture |
| read | SORECURDOCUMENT | SessionClient.read | done | unit, fixture |
| read | SOSUBTOTALTEMPLATE | SessionClient.read | done | unit, fixture |
| read | STANDARDCOSTTYPE | SessionClient.read | done | unit, fixture |
| read | STANDARDTASK | SessionClient.read | done | unit, fixture |
| read | STATACCOUNT | SessionClient.read | done | unit, fixture |
| read | TASK | SessionClient.read | done | unit, fixture |
| read | TASKRESOURCES | SessionClient.read | done | unit, fixture |
| read | TAXDETAIL | SessionClient.read | done | unit, fixture |
| read | TAXRECORD | SessionClient.read | done | unit, fixture |
| read | TAXSOLUTION | SessionClient.read | done | unit, fixture |
| read | TIMESHEET | SessionClient.read | done | unit, fixture |
| read | TIMESHEETAPPROVAL | SessionClient.read | done | unit, fixture |
| read | TIMESHEETENTRY | SessionClient.read | done | unit, fixture |
| read | TIMETYPE | SessionClient.read | done | unit, fixture |
| read | TRANSACTIONRULE | SessionClient.read | done | unit, fixture |
| read | TRANSACTIONRULEDETAIL | SessionClient.read | done | unit, fixture |
| read | UOM | SessionClient.read | done | unit, fixture |
| read | UOMDETAIL | SessionClient.read | done | unit, fixture |
| read | USERGROUP | SessionClient.read | done | unit, fixture |
| read | USERINFO | SessionClient.read | done | unit, fixture |
| read | USERRESTRICTION | SessionClient.read | done | unit, fixture |
| read | USERRIGHTS | SessionClient.read | done | unit, fixture |
| read | VENDOR | SessionClient.read | done | unit, fixture |
| read | VENDOREMAILTEMPLATE | SessionClient.read | done | unit, fixture |
| read | VENDORGROUP | SessionClient.read | done | unit, fixture |
| read | VENDORVISIBILITY | SessionClient.read | done | unit, fixture |
| read | VENDTYPE | SessionClient.read | done | unit, fixture |
| read | WAREHOUSE | SessionClient.read | done | unit, fixture |
| read | WAREHOUSEGROUP | SessionClient.read | done | unit, fixture |
| read | ZONE | SessionClient.read | done | unit, fixture |
| readByName | ACCUMULATIONTYPE | OperationClient.read_by_name | done | unit, fixture |
| readByName | ACHBANK | OperationClient.read_by_name | done | unit, fixture |
| readByName | AISLE | OperationClient.read_by_name | done | unit, fixture |
| readByName | ALLOCATION | OperationClient.read_by_name | done | unit, fixture |
| readByName | APACCOUNTLABEL | OperationClient.read_by_name | done | unit, fixture |
| readByName | APTERM | OperationClient.read_by_name | done | unit, fixture |
| readByName | ARACCOUNTLABEL | OperationClient.read_by_name | done | unit, fixture |
| readByName | ARTERM | OperationClient.read_by_name | done | unit, fixture |
| readByName | BIN | OperationClient.read_by_name | done | unit, fixture |
| readByName | BINFACE | OperationClient.read_by_name | done | unit, fixture |
| readByName | BINSIZE | OperationClient.read_by_name | done | unit, fixture |
| readByName | CHANGEREQUEST | OperationClient.read_by_name | done | unit, fixture |
| readByName | CHANGEREQUESTSTATUS | OperationClient.read_by_name | done | unit, fixture |
| readByName | CHANGEREQUESTTYPE | OperationClient.read_by_name | done | unit, fixture |
| readByName | CHECKINGACCOUNT | OperationClient.read_by_name | done | unit, fixture |
| readByName | CLASS | OperationClient.read_by_name | done | unit, fixture |
| readByName | CLASSGROUP | OperationClient.read_by_name | done | unit, fixture |
| readByName | COMPLIANCEDEFINITION | OperationClient.read_by_name | done | unit, fixture |
| readByName | COMPLIANCETYPE | OperationClient.read_by_name | done | unit, fixture |
| readByName | CONTACT | OperationClient.read_by_name | done | unit, fixture |
| readByName | CONTRACT | OperationClient.read_by_name | done | unit, fixture |
| readByName | CONTRACTBILLINGTEMPLATE | OperationClient.read_by_name | done | unit, fixture |
| readByName | CONTRACTEXPENSETEMPLATE | OperationClient.read_by_name | done | unit, fixture |
| readByName | CONTRACTGROUP | OperationClient.read_by_name | done | unit, fixture |
| readByName | CONTRACTMEAPRICELIST | OperationClient.read_by_name | done | unit, fixture |
| readByName | CONTRACTPRICELIST | OperationClient.read_by_name | done | unit, fixture |
| readByName | CONTRACTREVENUETEMPLATE | OperationClient.read_by_name | done | unit, fixture |
| readByName | CONTRACTTYPE | OperationClient.read_by_name | done | unit, fixture |
| readByName | CREDITCARD | OperationClient.read_by_name | done | unit, fixture |
| readByName | CUSTOMER | OperationClient.read_by_name | done | unit, fixture |
| readByName | CUSTOMEREMAILTEMPLATE | OperationClient.read_by_name | done | unit, fixture |
| readByName | CUSTOMERGROUP | OperationClient.read_by_name | done | unit, fixture |
| readByName | CUSTTYPE | OperationClient.read_by_name | done | unit, fixture |
| readByName | DEPARTMENT | OperationClient.read_by_name | done | unit, fixture |
| readByName | DEPARTMENTGROUP | OperationClient.read_by_name | done | unit, fixture |
| readByName | EARNINGTYPE | OperationClient.read_by_name | done | unit, fixture |
| readByName | EEACCOUNTLABEL | OperationClient.read_by_name | done | unit, fixture |
| readByName | EMPLOYEE | OperationClient.read_by_name | done | unit, fixture |
| readByName | EMPLOYEEGROUP | OperationClient.read_by_name | done | unit, fixture |
| readByName | EMPLOYEEPOSITION | OperationClient.read_by_name | done | unit, fixture |
| readByName | EMPLOYEETYPE | OperationClient.read_by_name | done | unit, fixture |
| readByName | EXCHANGERATETYPES | OperationClient.read_by_name | done | unit, fixture |
| readByName | EXPENSEPAYMENTTYPE | OperationClient.read_by_name | done | unit, fixture |
| readByName | GCBOOK | OperationClient.read_by_name | done | unit, fixture |
| readByName | GCOWNERSHIPSTRUCTURE | OperationClient.read_by_name | done | unit, fixture |
| readByName | GLACCOUNT | OperationClient.read_by_name | done | unit, fixture |
| readByName | GLACCTGRP | OperationClient.read_by_name | done | unit, fixture |
| readByName | GLACCTGRPPURPOSE | OperationClient.read_by_name | done | unit, fixture |
| readByName | GLBUDGETHEADER | OperationClient.read_by_name | done | unit, fixture |
| readByName | ICROW | OperationClient.read_by_name | done | unit, fixture |
| readByName | INVPRICELIST | OperationClient.read_by_name | done | unit, fixture |
| readByName | ITEM | OperationClient.read_by_name | done | unit, fixture |
| readByName | ITEMGLGROUP | OperationClient.read_by_name | done | unit, fixture |
| readByName | ITEMGROUP | OperationClient.read_by_name | done | unit, fixture |
| readByName | ITEMTAXGROUP | OperationClient.read_by_name | done | unit, fixture |
| readByName | LABORCLASS | OperationClient.read_by_name | done | unit, fixture |
| readByName | LABORSHIFT | OperationClient.read_by_name | done | unit, fixture |
| readByName | LABORUNION | OperationClient.read_by_name | done | unit, fixture |
| readByName | LOCATION | OperationClient.read_by_name | done | unit, fixture |
| readByName | LOCATIONENTITY | OperationClient.read_by_name | done | unit, fixture |
| readByName | LOCATIONGROUP | OperationClient.read_by_name | done | unit, fixture |
| readByName | PJESTIMATE | OperationClient.read_by_name | done | unit, fixture |
| readByName | PJESTIMATETYPE | OperationClient.read_by_name | done | unit, fixture |
| readByName | POPRICELIST | OperationClient.read_by_name | done | unit, fixture |
| readByName | POSITIONSKILL | OperationClient.read_by_name | done | unit, fixture |
| readByName | POSUBTOTALTEMPLATE | OperationClient.read_by_name | done | unit, fixture |
| readByName | PRODUCTLINE | OperationClient.read_by_name | done | unit, fixture |
| readByName | PROJECT | OperationClient.read_by_name | done | unit, fixture |
| readByName | PROJECTCHANGEORDER | OperationClient.read_by_name | done | unit, fixture |
| readByName | PROJECTCONTRACT | OperationClient.read_by_name | done | unit, fixture |
| readByName | PROJECTCONTRACTTYPE | OperationClient.read_by_name | done | unit, fixture |
| readByName | PROJECTGROUP | OperationClient.read_by_name | done | unit, fixture |
| readByName | PROJECTSTATUS | OperationClient.read_by_name | done | unit, fixture |
| readByName | PROJECTTYPE | OperationClient.read_by_name | done | unit, fixture |
| readByName | PTAPPLICATION | OperationClient.read_by_name | done | unit, fixture |
| readByName | RATETABLE | OperationClient.read_by_name | done | unit, fixture |
| readByName | REPORTINGPERIOD | OperationClient.read_by_name | done | unit, fixture |
| readByName | ROLES | OperationClient.read_by_name | done | unit, fixture |
| readByName | SAVINGSACCOUNT | OperationClient.read_by_name | done | unit, fixture |
| readByName | SOPRICELIST | OperationClient.read_by_name | done | unit, fixture |
| readByName | SOSUBTOTALTEMPLATE | OperationClient.read_by_name | done | unit, fixture |
| readByName | STANDARDCOSTTYPE | OperationClient.read_by_name | done | unit, fixture |
| readByName | STANDARDTASK | OperationClient.read_by_name | done | unit, fixture |
| readByName | STATACCOUNT | OperationClient.read_by_name | done | unit, fixture |
| readByName | TAXSOLUTION | OperationClient.read_by_name | done | unit, fixture |
| readByName | TIMETYPE | OperationClient.read_by_name | done | unit, fixture |
| readByName | TRANSACTIONRULE | OperationClient.read_by_name | done | unit, fixture |
| readByName | UOM | OperationClient.read_by_name | done | unit, fixture |
| readByName | USERINFO | OperationClient.read_by_name | done | unit, fixture |
| readByName | VENDOR | OperationClient.read_by_name | done | unit, fixture |
| readByName | VENDORGROUP | OperationClient.read_by_name | done | unit, fixture |
| readByName | VENDTYPE | OperationClient.read_by_name | done | unit, fixture |
| readByName | WAREHOUSE | OperationClient.read_by_name | done | unit, fixture |
| readByName | WAREHOUSEGROUP | OperationClient.read_by_name | done | unit, fixture |
| readByName | ZONE | OperationClient.read_by_name | done | unit, fixture |
| readByName | compliancerecord | OperationClient.read_by_name | done | unit, fixture |
| readByQuery | ACCTTITLEBYLOC | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | ACCUMULATIONTYPE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | ACHBANK | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | ACTIVITYLOG | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | ADVAUDITHISTORY | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | AISLE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | ALLOCATION | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | ALLOCATIONENTRY | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | APACCOUNTLABEL | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | APADJUSTMENT | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | APADJUSTMENTITEM | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | APBILL | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | APBILLBATCH | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | APBILLITEM | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | APBILLJOINTPAYEE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | APPAYMENTREQUEST | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | APPYMT | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | APPYMTDETAIL | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | APRECURBILL | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | APRECURBILLENTRY | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | APRETAINAGERELEASE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | APRETAINAGERELEASEENTRY | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | APTERM | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | ARACCOUNTLABEL | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | ARADJUSTMENT | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | ARADJUSTMENTITEM | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | ARADVANCE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | ARINVOICE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | ARINVOICEBATCH | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | ARPAYMENT | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | ARPYMT | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | ARRECURINVOICE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | ARRECURINVOICEENTRY | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | ARRETAINAGERELEASEENTRY | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | ARTERM | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | AUDITHISTORY | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | AVAILABLEINVENTORY | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | BANKACCTRECON | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | BANKACCTTXNFEED | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | BANKFEE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | BANKFEEENTRY | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | BIN | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | BINFACE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | BINSIZE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CCTRANSACTION | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CCTRANSACTIONENTRY | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CHANGEREQUEST | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CHANGEREQUESTENTRY | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CHANGEREQUESTSTATUS | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CHANGEREQUESTTYPE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CHARGEPAYOFF | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CHARGEPAYOFFENTRY | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CHECKINGACCOUNT | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CLASS | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CLASSGROUP | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | COGSCLOSEDJE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | COMPLIANCEDEFINITION | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | COMPLIANCETYPE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CONTACT | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CONTRACT | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CONTRACTBILLINGSCHEDULE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CONTRACTBILLINGSCHEDULEENTRY | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CONTRACTBILLINGTEMPLATE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CONTRACTBILLINGTEMPLATEENTRY | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CONTRACTDETAIL | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CONTRACTEXPENSE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CONTRACTEXPENSE2SCHEDULE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CONTRACTEXPENSESCHEDULE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CONTRACTEXPENSETEMPLATE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CONTRACTGROUP | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CONTRACTITEMPRCLSTENTYTIER | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CONTRACTITEMPRICELIST | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CONTRACTITEMPRICELISTENTRY | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CONTRACTMEABUNDLE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CONTRACTMEAITEMPRICELIST | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CONTRACTMEAITEMPRICELISTENTRY | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CONTRACTMEAPRICELIST | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CONTRACTPRICELIST | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CONTRACTREVENUE2SCHEDULE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CONTRACTREVENUESCHEDULE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CONTRACTREVENUETEMPLATE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CONTRACTTYPE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CONTRACTUSAGE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | COSTTYPE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CREDITCARD | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CREDITCARDFEE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CREDITCARDFEEENTRY | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CUSTOMER | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CUSTOMEREMAILTEMPLATE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CUSTOMERGROUP | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | CUSTTYPE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | DDSJOB | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | DEPARTMENT | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | DEPARTMENTGROUP | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | DEPOSIT | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | DEPOSITENTRY | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | EARNINGTYPE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | EEACCOUNTLABEL | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | EEXPENSES | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | EMPLOYEE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | EMPLOYEEGROUP | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | EMPLOYEEPOSITION | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | EMPLOYEETYPE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | EPPAYMENT | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | EPPAYMENTREQUEST | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | EXCHANGERATE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | EXCHANGERATEENTRY | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | EXCHANGERATETYPES | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | EXPENSEADJUSTMENTS | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | EXPENSEADJUSTMENTSITEM | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | EXPENSEPAYMENTTYPE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | FUNDSTRANSFER | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | FUNDSTRANSFERENTRY | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | GCBOOK | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | GCBOOKACCTRATETYPE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | GCBOOKADJJOURNAL | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | GCBOOKELIMACCOUNT | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | GCBOOKENTITY | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | GENINVOICEPOLICY | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | GENINVOICEPREVIEW | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | GENINVOICEPREVIEWLINE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | GENINVOICERUN | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | GLACCOUNT | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | GLACCOUNTBALANCE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | GLACCTALLOCATION | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | GLACCTALLOCATIONGRP | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | GLACCTALLOCATIONRUN | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | GLACCTGRP | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | GLACCTGRPHIERARCHY | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | GLACCTGRPPURPOSE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | GLBATCH | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | GLBUDGETHEADER | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | GLBUDGETITEM | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | GLDETAIL | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | GLENTRY | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | ICCYCLECOUNT | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | ICCYCLECOUNTENTRY | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | ICROW | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | ICTRANSFER | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | INVDOCUMENT | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | INVDOCUMENTENTRY | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | INVDOCUMENTPARAMS | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | INVDOCUMENTSUBTOTALS | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | INVENTORYTOTALDETAIL | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | INVPRICELIST | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | ITEM | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | ITEMCROSSREF | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | ITEMGLGROUP | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | ITEMGROUP | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | ITEMTAXGROUP | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | ITEMWAREHOUSEINFO | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | InventoryWQDetail | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | InventoryWQOrder | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | JOBQUEUERECORD | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | LABORCLASS | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | LABORSHIFT | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | LABORUNION | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | LOCATION | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | LOCATIONENTITY | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | LOCATIONGROUP | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | MEMBERUSERGROUP | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | OBSPCTCOMPLETED | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | OTHERRECEIPTS | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | OTHERRECEIPTSENTRY | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | PJESTIMATE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | PJESTIMATEENTRY | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | PJESTIMATETYPE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | PODOCUMENT | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | PODOCUMENTENTRY | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | PODOCUMENTPARAMS | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | PODOCUMENTSUBTOTALS | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | POPRICELIST | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | POSITIONSKILL | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | POSUBTOTALTEMPLATE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | PRODUCTLINE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | PROJECT | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | PROJECTCHANGEORDER | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | PROJECTGROUP | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | PROJECTRESOURCES | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | PROJECTSTATUS | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | PROJECTTYPE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | PROVIDERBANKACCOUNT | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | PROVIDERPAYMENTMETHOD | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | PROVIDERVENDOR | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | PTAPPLICATION | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | RECURGLACCTALLOCATION | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | REPORTINGPERIOD | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | REVRECSCHEDULE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | REVRECSCHEDULEENTRY | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | ROLEASSIGNMENT | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | ROLEGROUPS | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | ROLEPOLICYASSIGNMENT | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | ROLES | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | ROLEUSERS | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | SAVINGSACCOUNT | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | SODOCUMENT | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | SODOCUMENTENTRY | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | SODOCUMENTPARAMS | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | SODOCUMENTSUBTOTALS | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | SOPRICELIST | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | SORECURDOCUMENT | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | SOSUBTOTALTEMPLATE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | STANDARDCOSTTYPE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | STANDARDTASK | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | STATACCOUNT | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | TASK | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | TASKRESOURCES | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | TAXDETAIL | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | TAXRECORD | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | TAXSOLUTION | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | TIMESHEET | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | TIMESHEETENTRY | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | TIMETYPE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | TRANSACTIONRULE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | TRANSACTIONRULEDETAIL | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | UOM | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | UOMDETAIL | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | USERGROUP | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | USERINFO | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | USERRESTRICTION | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | USERRIGHTS | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | USERROLES | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | VENDOR | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | VENDOREMAILTEMPLATE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | VENDORGROUP | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | VENDTYPE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | WAREHOUSE | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | WAREHOUSEGROUP | SessionClient.read_by_query | done | unit, fixture |
| readByQuery | ZONE | SessionClient.read_by_query | done | unit, fixture |
| readEntityDetails | Company and Console | OperationClient.read_entity_details | done | unit, fixture |
| readMore | Customization Services | OperationClient.read_more | done | unit, fixture |
| readRelated | asset | OperationClient.read_related | done | unit, fixture |
| readReport | Customization Services | OperationClient.read_report | done | unit, fixture |
| readReport | General Ledger | OperationClient.read_report | done | unit, fixture |
| readUserFormatting | Company and Console | OperationClient.read_user_formatting | done | unit, fixture |
| readView | Platform Services | OperationClient.read_view | done | unit, fixture |
| reallocate | CONTRACTEXPENSE2SCHEDULE | OperationClient.reallocate | done | unit, fixture |
| reallocate | CONTRACTEXPENSESCHEDULE | OperationClient.reallocate | done | unit, fixture |
| reallocate | CONTRACTREVENUE2SCHEDULE | OperationClient.reallocate | done | unit, fixture |
| reallocate | CONTRACTREVENUESCHEDULE | OperationClient.reallocate | done | unit, fixture |
| reallocate_revrecschedule | Order Entry | OperationClient.reallocate_revrecschedule | done | unit, fixture |
| reconcile_bank | Cash Management | OperationClient.reconcile_bank | done | unit, fixture |
| record_cctransaction | Cash Management | OperationClient.record_cctransaction | done | unit, fixture |
| record_deposit | Cash Management | OperationClient.record_deposit | done | unit, fixture |
| record_otherreceipt | Cash Management | OperationClient.record_otherreceipt | done | unit, fixture |
| renew | CONTRACT | OperationClient.renew | done | unit, fixture |
| resume | CONTRACTDETAIL | OperationClient.resume | done | unit, fixture |
| resume | CONTRACTEXPENSE | OperationClient.resume | done | unit, fixture |
| resume_revrecschedule | Order Entry | OperationClient.resume_revrecschedule | done | unit, fixture |
| retrievepdf | ARINVOICE | OperationClient.retrievepdf | done | unit, fixture |
| retrievepdf | SODOCUMENT | OperationClient.retrievepdf | done | unit, fixture |
| reverse_appayment | Accounts Payable | OperationClient.reverse_appayment | done | unit, fixture |
| reverse_arpayment | Accounts Receivable | OperationClient.reverse_arpayment | done | unit, fixture |
| reverse_bill | Accounts Payable | OperationClient.reverse_bill | done | unit, fixture |
| reverse_cctransaction | Cash Management | OperationClient.reverse_cctransaction | done | unit, fixture |
| reverse_expensereport | Employee Expenses | OperationClient.reverse_expensereport | done | unit, fixture |
| reverse_invoice | Accounts Receivable | OperationClient.reverse_invoice | done | unit, fixture |
| runDdsJob | VENDOR | OperationClient.run_dds_job | done | unit, fixture |
| send_appaymentrequest | Accounts Payable | OperationClient.send_appaymentrequest | done | unit, fixture |
| terminate_revrecschedule | Order Entry | OperationClient.terminate_revrecschedule | done | unit, fixture |
| unpost | CONTRACTEXPENSESCHEDULEENTRY | OperationClient.unpost | done | unit, fixture |
| unpost | CONTRACTREVENUESCHEDULEENTRY | OperationClient.unpost | done | unit, fixture |
| unpost_revrecscheduleentry | Order Entry | OperationClient.unpost_revrecscheduleentry | done | unit, fixture |
| update | ACCUMULATIONTYPE | SessionClient.update | done | unit, fixture |
| update | AFRSETUP | SessionClient.update | done | unit, fixture |
| update | ALLOCATION | SessionClient.update | done | unit, fixture |
| update | APACCOUNTLABEL | SessionClient.update | done | unit, fixture |
| update | APBILL | SessionClient.update | done | unit, fixture |
| update | APBILLJOINTPAYEE | SessionClient.update | done | unit, fixture |
| update | APPYMT | SessionClient.update | done | unit, fixture |
| update | APRETAINAGERELEASE | SessionClient.update | done | unit, fixture |
| update | ARACCOUNTLABEL | SessionClient.update | done | unit, fixture |
| update | ARADVANCE | SessionClient.update | done | unit, fixture |
| update | ARPYMT | SessionClient.update | done | unit, fixture |
| update | ARRETAINAGERELEASE | SessionClient.update | done | unit, fixture |
| update | BIN | SessionClient.update | done | unit, fixture |
| update | BINFACE | SessionClient.update | done | unit, fixture |
| update | BINSIZE | SessionClient.update | done | unit, fixture |
| update | CHANGEREQUEST | SessionClient.update | done | unit, fixture |
| update | CHANGEREQUESTSTATUS | SessionClient.update | done | unit, fixture |
| update | CHANGEREQUESTTYPE | SessionClient.update | done | unit, fixture |
| update | CLASS | SessionClient.update | done | unit, fixture |
| update | COMPLIANCEDEFINITION | SessionClient.update | done | unit, fixture |
| update | COMPLIANCERECORD | SessionClient.update | done | unit, fixture |
| update | COMPLIANCETYPE | SessionClient.update | done | unit, fixture |
| update | CONTACT | SessionClient.update | done | unit, fixture |
| update | CONTRACT | SessionClient.update | done | unit, fixture |
| update | CONTRACTBILLINGSCHEDULE | SessionClient.update | done | unit, fixture |
| update | CONTRACTBILLINGTEMPLATE | SessionClient.update | done | unit, fixture |
| update | CONTRACTDETAIL | SessionClient.update | done | unit, fixture |
| update | CONTRACTEXPENSE | SessionClient.update | done | unit, fixture |
| update | CONTRACTEXPENSETEMPLATE | SessionClient.update | done | unit, fixture |
| update | CONTRACTPRICELIST | SessionClient.update | done | unit, fixture |
| update | CONTRACTREVENUETEMPLATE | SessionClient.update | done | unit, fixture |
| update | CONTRACTTYPE | SessionClient.update | done | unit, fixture |
| update | CONTRACTUSAGE | SessionClient.update | done | unit, fixture |
| update | COSTTYPE | SessionClient.update | done | unit, fixture |
| update | CUSTOMER | SessionClient.update | done | unit, fixture |
| update | Consolidations | SessionClient.update | done | unit, fixture |
| update | DEPARTMENT | SessionClient.update | done | unit, fixture |
| update | DUNNINGDEFINITION | SessionClient.update | done | unit, fixture |
| update | EEACCOUNTLABEL | SessionClient.update | done | unit, fixture |
| update | EMPLOYEE | SessionClient.update | done | unit, fixture |
| update | EMPLOYEEPOSITION | SessionClient.update | done | unit, fixture |
| update | GCBOOK | SessionClient.update | done | unit, fixture |
| update | GCBOOKACCTRATETYPE | SessionClient.update | done | unit, fixture |
| update | GCBOOKADJJOURNAL | SessionClient.update | done | unit, fixture |
| update | GCOWNERSHIPSTRUCTURE | SessionClient.update | done | unit, fixture |
| update | GENINVOICEPOLICY | SessionClient.update | done | unit, fixture |
| update | GLACCOUNT | SessionClient.update | done | unit, fixture |
| update | GLACCTALLOCATION | SessionClient.update | done | unit, fixture |
| update | GLACCTALLOCATIONGRP | SessionClient.update | done | unit, fixture |
| update | GLACCTGRP | SessionClient.update | done | unit, fixture |
| update | GLACCTGRPPURPOSE | SessionClient.update | done | unit, fixture |
| update | GLBATCH | SessionClient.update | done | unit, fixture |
| update | GLBUDGETHEADER | SessionClient.update | done | unit, fixture |
| update | ICCYCLECOUNTENTRY | SessionClient.update | done | unit, fixture |
| update | ICTRANSFER | SessionClient.update | done | unit, fixture |
| update | INTERENTITYSETUP | SessionClient.update | done | unit, fixture |
| update | ITEM | SessionClient.update | done | unit, fixture |
| update | ITEMCROSSREF | SessionClient.update | done | unit, fixture |
| update | LABORCLASS | SessionClient.update | done | unit, fixture |
| update | LABORSHIFT | SessionClient.update | done | unit, fixture |
| update | LABORUNION | SessionClient.update | done | unit, fixture |
| update | LOCATION | SessionClient.update | done | unit, fixture |
| update | OBSPCTCOMPLETED | SessionClient.update | done | unit, fixture |
| update | PAYROLLREPORTCHECK | SessionClient.update | done | unit, fixture |
| update | PAYROLLREPORTEMPLOYEE | SessionClient.update | done | unit, fixture |
| update | PAYROLLREPORTGROSSPAY | SessionClient.update | done | unit, fixture |
| update | PAYROLLREPORTPAYMODIFIER | SessionClient.update | done | unit, fixture |
| update | PAYROLLREPORTPTOACCRUALSCHEDULE | SessionClient.update | done | unit, fixture |
| update | PAYROLLREPORTPTOACTIVITY | SessionClient.update | done | unit, fixture |
| update | PAYROLLREPORTTAX | SessionClient.update | done | unit, fixture |
| update | PAYROLLREPORTTAXSETUP | SessionClient.update | done | unit, fixture |
| update | PAYROLLREPORTTIMECARD | SessionClient.update | done | unit, fixture |
| update | PAYROLLREPORTTRADE | SessionClient.update | done | unit, fixture |
| update | PJESTIMATE | SessionClient.update | done | unit, fixture |
| update | PJESTIMATEENTRY | SessionClient.update | done | unit, fixture |
| update | PJESTIMATETYPE | SessionClient.update | done | unit, fixture |
| update | PROJECT | SessionClient.update | done | unit, fixture |
| update | PROJECTCHANGEORDER | SessionClient.update | done | unit, fixture |
| update | PROJECTCONTRACT | SessionClient.update | done | unit, fixture |
| update | PROJECTCONTRACTLINE | SessionClient.update | done | unit, fixture |
| update | PROJECTCONTRACTTYPE | SessionClient.update | done | unit, fixture |
| update | PROVIDERBANKACCOUNT | SessionClient.update | done | unit, fixture |
| update | PROVIDERVENDOR | SessionClient.update | done | unit, fixture |
| update | RATETABLE | SessionClient.update | done | unit, fixture |
| update | REPORTINGPERIOD | SessionClient.update | done | unit, fixture |
| update | STANDARDCOSTTYPE | SessionClient.update | done | unit, fixture |
| update | STANDARDTASK | SessionClient.update | done | unit, fixture |
| update | STATACCOUNT | SessionClient.update | done | unit, fixture |
| update | TASK | SessionClient.update | done | unit, fixture |
| update | TAXRECORD | SessionClient.update | done | unit, fixture |
| update | TIMESHEET | SessionClient.update | done | unit, fixture |
| update | USERINFO | SessionClient.update | done | unit, fixture |
| update | VENDOR | SessionClient.update | done | unit, fixture |
| update | WAREHOUSE | SessionClient.update | done | unit, fixture |
| update | ZONE | SessionClient.update | done | unit, fixture |
| update_achbankconfiguration | Cash Management | OperationClient.update_achbankconfiguration | done | unit, fixture |
| update_apaccountlabel | Accounts Payable | OperationClient.update_apaccountlabel | done | unit, fixture |
| update_apadjustment | Accounts Payable | OperationClient.update_apadjustment | done | unit, fixture |
| update_apterm | Accounts Payable | OperationClient.update_apterm | done | unit, fixture |
| update_araccountlabel | Accounts Receivable | OperationClient.update_araccountlabel | done | unit, fixture |
| update_aradjustment | Accounts Receivable | OperationClient.update_aradjustment | done | unit, fixture |
| update_arterm | Accounts Receivable | OperationClient.update_arterm | done | unit, fixture |
| update_bill | Accounts Payable | OperationClient.update_bill | done | unit, fixture |
| update_cctransaction | Cash Management | OperationClient.update_cctransaction | done | unit, fixture |
| update_class | Company and Console | OperationClient.update_class | done | unit, fixture |
| update_contact | Company and Console | OperationClient.update_contact | done | unit, fixture |
| update_customer | Accounts Receivable | OperationClient.update_customer | done | unit, fixture |
| update_customerbankaccount | Accounts Receivable | OperationClient.update_customerbankaccount | done | unit, fixture |
| update_customerchargecard | Accounts Receivable | OperationClient.update_customerchargecard | done | unit, fixture |
| update_department | Company and Console | OperationClient.update_department | done | unit, fixture |
| update_earningtype | Project Resource Management | OperationClient.update_earningtype | done | unit, fixture |
| update_employee | Employee Expenses | OperationClient.update_employee | done | unit, fixture |
| update_employeerate | Employee Expenses | OperationClient.update_employeerate | done | unit, fixture |
| update_expenseadjustmentreport | Employee Expenses | OperationClient.update_expenseadjustmentreport | done | unit, fixture |
| update_expensepaymenttype | Employee Expenses | OperationClient.update_expensepaymenttype | done | unit, fixture |
| update_expensereport | Employee Expenses | OperationClient.update_expensereport | done | unit, fixture |
| update_expensetype | Employee Expenses | OperationClient.update_expensetype | done | unit, fixture |
| update_glaccount | General Ledger | OperationClient.update_glaccount | done | unit, fixture |
| update_ictransaction | Inventory Control | OperationClient.update_ictransaction | done | unit, fixture |
| update_invoice | Accounts Receivable | OperationClient.update_invoice | done | unit, fixture |
| update_item | Inventory Control | OperationClient.update_item | done | unit, fixture |
| update_location | Company and Console | OperationClient.update_location | done | unit, fixture |
| update_otherreceipt | Cash Management | OperationClient.update_otherreceipt | done | unit, fixture |
| update_popricelist | Purchasing | OperationClient.update_popricelist | done | unit, fixture |
| update_potransaction | Purchasing | OperationClient.update_potransaction | done | unit, fixture |
| update_revrecschedule | Order Entry | OperationClient.update_revrecschedule | done | unit, fixture |
| update_savingsaccount | Cash Management | OperationClient.update_savingsaccount | done | unit, fixture |
| update_sopricelist | Order Entry | OperationClient.update_sopricelist | done | unit, fixture |
| update_sotransaction | Order Entry | OperationClient.update_sotransaction | done | unit, fixture |
| update_statglaccount | General Ledger | OperationClient.update_statglaccount | done | unit, fixture |
| update_supdoc | Company and Console | OperationClient.update_supdoc | done | unit, fixture |
| update_supdocfolder | Company and Console | OperationClient.update_supdocfolder | done | unit, fixture |
| update_task | Project Resource Management | OperationClient.update_task | done | unit, fixture |
| update_territory | Accounts Receivable | OperationClient.update_territory | done | unit, fixture |
| update_timesheet | Project Resource Management | OperationClient.update_timesheet | done | unit, fixture |
| update_timetype | Project Resource Management | OperationClient.update_timetype | done | unit, fixture |
| update_vendor | Accounts Payable | OperationClient.update_vendor | done | unit, fixture |
| void_appaymentrequest | Accounts Payable | OperationClient.void_appaymentrequest | done | unit, fixture |

## Notes
- Generated from Postman collections in `Docs/`. Review for accuracy before implementation.
