import boto3
session=boto3.session.Session(profile_name="augie-admin")
iam_re_user=session.resource(service_name="iam", region_name="ap-south-1")
iam_user=input("Enter Iam User Details: ")
required_iam_user=iam_re_user.User(iam_user)
print("Iam User Details")
try:
    print ("User Name: {}\nUserCreation: {}\n".format(required_iam_user.user_name, required_iam_user.create_date))
except Exception as e:
    print(e.response['Error']['Code'])
    
    OUTPUT : 
    
    Enter Iam User Details: dsd
Iam User Details
NoSuchEntity

Process finished with exit code 0
