#!/bin/bash
aws s3 mb s3://my-static-site-$(date +%s) --region ap-northeast-1
aws s3 sync . s3://my-static-site --acl public-read
