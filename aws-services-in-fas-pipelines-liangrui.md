
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
 Storage & Data | S3 | Bucket Policies | Yes
 Storage & Data | S3 | Versioning | Yes
 Storage & Data | S3 | Encryption | Yes
 Storage & Data | S3 | Event Notifications | Yes
 Storage & Data | RDS | PostgreSQL Instance | Yes
 Storage & Data | RDS | Subnet Groups | Yes
 Storage & Data | DynamoDB | Tables | Yes
 Storage & Data | DynamoDB | Global Secondary Indexes | Yes
 Storage & Data | ElastiCache | Memcached Cluster | Yes
 Storage & Data | ElastiCache | Subnet Groups | Yes
 Storage & Data | OpenSearch | Engine Version: 7.10 | Yes
 Storage & Data | OpenSearch | Deployed in VPC | Yes
 Storage & Data | Glue | Crawler | Yes
 Storage & Data | Glue | Catalog DB | Yes
 Storage & Data | Glue | Catalog Table | Yes
 Integration and Serverless | CloudWatch | Log Groups | Yes
 Integration and Serverless | CloudWatch | Event Rules | Yes
 Integration and Serverless | CloudWatch | Alarms | Yes
 Integration and Serverless | CloudWatch | Dashboards | Yes
 Integration and Serverless | Step Functions | All | Yes
 Integration and Serverless | SNS | All | Yes
 Integration and Serverless | SQS | FIFO as well | Yes
 Integration and Serverless | Lambda | Function Runtimes: Python, NodeJS, Java | Yes
 Integration and Serverless | Lambda | Layers | Yes
 Integration and Serverless | Lambda | Triggers: SQS, SNS, API Gateway, Step Functions | Yes
 Integration and Serverless | Lambda | Also deployed in VPC | Yes
 Dev Tools | CodeCommit | All | Yes
 Dev Tools | CodeBuild | All | Yes
 Dev Tools | CodeArtifact | Domains | Yes
 Dev Tools | CodeArtifact | Repositories | Yes
