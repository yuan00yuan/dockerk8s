
Catalog | Services | Feature | Avaibility |
---------|----------|--------- | ---------
 Security | IAM | Roles | Yes
 Security | IAM | Policies | Yes
 Security | IAM | Instance Profiles | Yes
 Security | Secrets Manager | All | Yes
 Security | KMS | CMK | Yes
 Security | KMS | Aliases | Yes
 Security | KMS | Access Grants | Yes
 Security | Certificate Manager | Import certificates | Yes
 Security | Cognito | User Pools | No, using Okta, Keycloak
 Security | Cognito | Identity Pools | Yes
 Security | WAF | Regex Pattern Sets | Yes
 Security | WAF | Web ACL | Yes
 Network | Route 53 | Record types: "A", "CNAME" | Yes
 Network | VPC | Multiple CIDRs | Yes
 Network | VPC | Elastic IPs | Yes
 Network | VPC | Security Groups | Yes
 Network | VPC | Endpoints S3 (gateway) | Yes
 Network | VPC | Endpoints DynamoDB (gateway) | Yes
 Network | VPC | Endpoints EMR (interface) | Yes? I found both china and global only emr-container
 Network | VPC | Endpoints ECR API (interface) | Yes
 Network | VPC | Endpoints ECR DKR (interface) | Yes
 Network | VPC | Endpoints Logs (interface) | Yes
 Network | VPC | Endpoints SSM (interface) | Yes
 Network | VPC | Transit Gateways | Yes
 Network | VPC | NAT Gateways | Yes for both public and private
 Network | VPC | API Gateway - Usage Plans | Yes
 Network | VPC | API Gateway - API keys | Yes
 Network | VPC | API Gateway - Authorizers | Yes, no User Pool
 Network | VPC | API Gateway - Request Validators | Yes
 Network | VPC | API Gateway - Integrations - Lambda | Yes
 Network | VPC | API Gateway - Integrations - SQS | Yes
 Network | VPC | API Gateway - Integrations - Step Functions | Yes
 Compute | EC2 | Instances | Yes
 Compute | EC2 | Auto Scaling Groups | Yes
 Compute | ELB | Listeners | Yes
 Compute | ELB | Certificates | Yes
 Compute | ELB | Target Groups | Yes
 Compute | ELB | Health Checks | Yes
 Compute | ECR | All | Yes
 Compute | ECS | Cluster | Yes
 Compute | ECS | Service | Yes
 Compute | ECS | Task Definitions | Yes
 Compute | ECS | Service Discovery | Yes, CloudMap and AppMesh
 Compute | ECS | Service Discovery | Yes, CloudMap and AppMesh

### Storage & Data

- S3
    - Bucket Policies
    - Versioning
    - Encryption
    - Event Notifications

- RDS
    - PostgreSQL Instance
    - Subnet Groups

- DynamoDB
    - Tables
    - Global Secondary Indexes

- ElastiCache
    - Memcached Cluster
    - Subnet Groups

- OpenSearch
    - Engine Version: 7.10
    - Deployed in VPC

- Glue
    - Crawler
    - Catalog DB
    - Catalog Table


### Integration and Serverless

- CloudWatch
    - Log Groups
    - Event Rules
    - Alarms
    - Dashboards

- Step Functions

- SNS

- SQS
    - FIFO as well

- Lambda
    - Function Runtimes: Python, NodeJS, Java
    - Layers
    - Triggers: SQS, SNS, API Gateway, Step Functions
    - Also deployed in VPC


### Dev Tools

- CodeCommit

- CodeBuild

- CodeArtifact
    - Domains
    - Repositories
