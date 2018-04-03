from payir import payment

# Set Api Key
pay = payment("test")

# Get TransactionId and Transaction Url

# GetTransId(Price,CallbackUrl,FactNumber)
transid , url = pay.GetTransId("4000","http://domainname.com","1245")

# Verify Transaction . If transactios is true return 'ok' else return 'faild'

#VerifyTrans(transId)
result = pay.VerifyTrans("364")
