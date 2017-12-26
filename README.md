Welcome to the Cube Me Program!
==============================================

This is a Python application deployed to AWS Lambda to be run as a serverless function, invoked by a RESTful endpoint exposed by API Gateway.  The deployment pipeline consists of AWS CodeBuild which packages the application with all of its dependencies and Cloudformation which deploys the application to Lambda and API Gateway. It will take a curl command entry and return the cube of the number.

Curl Command:

curl -XPOST 'https://dhlbfd98j6.execute-api.us-east-1.amazonaws.com/Prod/' -d '{"number_to_cube":90}'

What's Here
-----------

This sample includes:

* README.md - this file
* buildspec.yml - this file is used by AWS CodeBuild to package your
  application for deployment to AWS Lambda
* index.py - this file contains the sample Python code for the web service
* template.yml - this file contains the Serverless Application Model (SAM) used
  by AWS Cloudformation to deploy your application to AWS Lambda and Amazon API
  Gateway.


What Do I Do Next?
------------------

If you have checked out a local copy of your repository you can start making changes
to the sample code.  We suggest making a small change to index.py first, so you can
see how changes pushed to your project's repository are automatically picked up by your
project pipeline and deployed to AWS Lambda and Amazon API Gateway. (You can watch the pipeline
progress on your AWS CodeStar project dashboard.)Once you've seen how that works,
start developing your own code, and have fun!

Learn more about Serverless Application Model (SAM) and how it works here:
https://github.com/awslabs/serverless-application-model/blob/master/HOWTO.md

AWS Lambda Developer Guide:
http://docs.aws.amazon.com/lambda/latest/dg/deploying-lambda-apps.html

Learn more about AWS CodeStar by reading the user guide, and post questions and
comments about AWS CodeStar on our forum.

AWS CodeStar User Guide:
http://docs.aws.amazon.com/codestar/latest/userguide/welcome.html

AWS CodeStar Forum: https://forums.aws.amazon.com/forum.jspa?forumID=248
