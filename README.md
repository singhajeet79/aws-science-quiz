# AWS Science Quiz Starter

Starter repo for a 10-question online science quiz hosted on AWS (free tier friendly).

## Structure
- backend/: Lambda function code (Python)
- frontend/: HTML/JS quiz UI
- infrastructure/: CloudFormation/SAM template


### Frontend (S3 + CloudFront)
1- Build a small static JS app that:\
   - lets each student enter school code + roll number (or Cognito sign-in).\
   - shows 10 questions, one page.\
   - posts answers to /submit endpoint (API Gateway).\
   - shows final score after submission (optionally calculated on server).
2- Host build on an S3 bucket configured for static website hosting (or host behind CloudFront for HTTPS).\
3- Create CloudFront distribution with the S3 bucket as origin; enable HTTPS and set cache rules (no caching for API calls — only static assets). CloudFront has free tier allowances; still good to use for performance. 
