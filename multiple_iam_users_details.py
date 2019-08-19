import boto3
session=boto3.session.Session(profile_name="augie-admin")
iam_re=session.resource(service_name="iam", region_name="ap-south-1")
print("*************  Resource Method  ***********")
for each_user in iam_re.users.all():
    #print(each_user.user_name, each_user.user_id,each_user.arn, each_user.create_date)
    print("UserName: {}\nuser ID: {}\nUser ARN: {}\nuser creation Date: {}".format(each_user.user_name, each_user.user_id, each_user.arn, each_user.create_date))

print("*************  Client Method  ***********")
iam_cli=session.client(service_name="iam", region_name="ap-south-1")
for each_use in iam_cli.list_users()['Users']:
    print(each_use['UserName'])
    
    
    OUTPUT : 
    
    *************  Resource Method  ***********
UserName: augie-admin
user ID: AIDAIMCJKWMDI2ADQ6ESE
User ARN: arn:aws:iam::974423882178:user/augie-admin
user creation Date: 2019-03-26 15:34:16+00:00
UserName: augie-cli
user ID: AIDA6FPWEHBEWCHASK37
User ARN: arn:aws:iam::97142334388217:user/augie-cli
user creation Date: 2019-04-01 16:20:57+00:00

*************  Client Method  ***********
augie-admin
augie-cli
botocli
cli_billa
