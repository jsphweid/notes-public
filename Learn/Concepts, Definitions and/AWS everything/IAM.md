# IAM

Policies - can be attached to [[Principals]] or [[Resources]]

- Types
    - Principals - **Identity Based Policy** - who you are
        - Managed Policies
            - AWS Managed
            - Customer Managed
        - Inline Policies
    - Resources - **Resource Based Policy**
        - Inline Policies
- Structure
    - Version
    - Statement
        - a policy with multiple statements applies a logical `or`
        - items
            - Efffect
            - Action
            - Resource (for Identity Based Policies)
            - Principal (for Resource Based Policies)
            - Condition
            

If there are conflicting policies, deny takes precedencex

Principals

- Users
- Groups
- Roles - can be assumed by just about anything it seems
    - when it comes to users assuming roles, temporary security credentials are created and 'provided to the user'
        - ec2 roles are a special type of 'service role'
    - you can assume a role, and use that role to assume another role
    - delegation - the granting of permissions so someone to allow access to resources you control
    - federation - a trust relationship between an external identity provider and AWS
    - trust policy - you define who can assume a role
    - permission policy - you define which resources the role can use
    - cross account roles - using a role from another account

Resources

- S3
- DynamoDB
- etc.

No one has permissions by default unless specifically allowed

IAM Access Analyzer - tool that let's you see S3 Buckets or IAM roles that are shared with an external entity