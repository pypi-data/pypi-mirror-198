'''
# aws-lambda-ssmstringparameter module

<!--BEGIN STABILITY BANNER-->---


![Stability: Experimental](https://img.shields.io/badge/stability-Experimental-important.svg?style=for-the-badge)

> All classes are under active development and subject to non-backward compatible changes or removal in any
> future version. These are not subject to the [Semantic Versioning](https://semver.org/) model.
> This means that while you may use them, you may need to update your source code when upgrading to a newer version of this package.

---
<!--END STABILITY BANNER-->

| **Reference Documentation**:| <span style="font-weight: normal">https://docs.aws.amazon.com/solutions/latest/constructs/</span>|
|:-------------|:-------------|

<div style="height:8px"></div>

| **Language**     | **Package**        |
|:-------------|-----------------|
|![Python Logo](https://docs.aws.amazon.com/cdk/api/latest/img/python32.png) Python|`aws_solutions_constructs.aws_lambda_ssm_string_parameter`|
|![Typescript Logo](https://docs.aws.amazon.com/cdk/api/latest/img/typescript32.png) Typescript|`@aws-solutions-constructs/aws-lambda-ssmstringparameter`|
|![Java Logo](https://docs.aws.amazon.com/cdk/api/latest/img/java32.png) Java|`software.amazon.awsconstructs.services.lambdassmstringparameter`|

## Overview

This AWS Solutions Construct implements the AWS Lambda function and AWS Systems Manager Parameter Store String parameter with the least privileged permissions.

Here is a minimal deployable pattern definition:

Typescript

```python
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { LambdaToSsmstringparameterProps,  LambdaToSsmstringparameter } from '@aws-solutions-constructs/aws-lambda-ssmstringparameter';
import * as lambda from 'aws-cdk-lib/aws-lambda';

const constructProps: LambdaToSsmstringparameterProps = {
  lambdaFunctionProps: {
    runtime: lambda.Runtime.NODEJS_14_X,
    code: lambda.Code.fromAsset(`lambda`),
    handler: 'index.handler'
  },
  stringParameterProps: { stringValue: "test-string-value" }
};

new LambdaToSsmstringparameter(this, 'test-lambda-ssmstringparameter-stack', constructProps);
```

Python

```python
from aws_solutions_constructs.aws_lambda_ssmstringparameter import LambdaToSsmstringparameter
from aws_cdk import (
    aws_lambda as _lambda,
    aws_ssm as ssm,
    Stack
)
from constructs import Construct

LambdaToSsmstringparameter(
    self, 'test-lambda-ssmstringparameter-stack',
    lambda_function_props=_lambda.FunctionProps(
        code=_lambda.Code.from_asset('lambda'),
        runtime=_lambda.Runtime.PYTHON_3_9,
        handler='index.handler'
    ),
    string_parameter_props=ssm.StringParameterProps(
        string_value="test-string-value")
)
```

Java

```java
import software.constructs.Construct;

import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awscdk.services.lambda.*;
import software.amazon.awscdk.services.lambda.Runtime;
import software.amazon.awscdk.services.ssm.*;
import software.amazon.awsconstructs.services.lambdassmstringparameter.*;

new LambdaToSsmstringparameter(this, "test-lambda-ssmstringparameter-stack",
        new LambdaToSsmstringparameterProps.Builder()
                .lambdaFunctionProps(new FunctionProps.Builder()
                        .runtime(Runtime.NODEJS_14_X)
                        .code(Code.fromAsset("lambda"))
                        .handler("index.handler")
                        .build())
                .stringParameterProps(new StringParameterProps.Builder()
                        .stringValue("test-string-value")
                        .build())
                .build());
```

## Pattern Construct Props

| **Name**     | **Type**        | **Description** |
|:-------------|:----------------|-----------------|
|existingLambdaObj?|[`lambda.Function`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html)|Existing instance of Lambda Function object, providing both this and `lambdaFunctionProps` will cause an error.|
|lambdaFunctionProps?|[`lambda.FunctionProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.FunctionProps.html)|User provided props to override the default props for the Lambda function.|
|existingStringParameterObj?|[`ssm.StringParameter`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ssm.StringParameter.html)|Existing instance of SSM String parameter object, providing both this and `stringParameterProps` will cause an error|
|stringParameterProps?|[`ssm.StringParameterProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ssm.StringParameterProps.html)|Optional user provided props to override the default props for SSM String parameter. If existingStringParameterObj is not set stringParameterProps is required. The only supported [`ssm.StringParameterProps.type`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ssm.StringParameterProps.html#type) is [`STRING`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ssm.ParameterType.html#string) if a different value is provided it will be overridden.|
|stringParameterEnvironmentVariableName?|`string`|Optional Name for the Lambda function environment variable set to the name of the parameter. Default: SSM_STRING_PARAMETER_NAME |
|existingVpc?|[`ec2.IVpc`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.IVpc.html)|An optional, existing VPC into which this pattern should be deployed. When deployed in a VPC, the Lambda function will use ENIs in the VPC to access network resources and an Interface Endpoint will be created in the VPC for AWS Systems Manager Parameter. If an existing VPC is provided, the `deployVpc` property cannot be `true`. This uses `ec2.IVpc` to allow clients to supply VPCs that exist outside the stack using the [`ec2.Vpc.fromLookup()`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.Vpc.html#static-fromwbrlookupscope-id-options) method.|
|vpcProps?|[`ec2.VpcProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.VpcProps.html)|Optional user-provided properties to override the default properties for the new VPC. `enableDnsHostnames`, `enableDnsSupport`, `natGateways` and `subnetConfiguration` are set by the pattern, so any values for those properties supplied here will be overrriden. If `deployVpc` is not `true` then this property will be ignored.|
|deployVpc?|`boolean`|Whether to create a new VPC based on `vpcProps` into which to deploy this pattern. Setting this to true will deploy the minimal, most private VPC to run the pattern:<ul><li> One isolated subnet in each Availability Zone used by the CDK program</li><li>`enableDnsHostnames` and `enableDnsSupport` will both be set to true</li></ul>If this property is `true` then `existingVpc` cannot be specified. Defaults to `false`.|
|stringParameterPermissions|`string`|Optional SSM String parameter permissions to grant to the Lambda function. One of the following may be specified: "Read", "ReadWrite".

## Pattern Properties

| **Name**     | **Type**        | **Description** |
|:-------------|:----------------|-----------------|
|lambdaFunction|[`lambda.Function`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html)|Returns an instance of lambda.Function created by the construct|
|stringParameter|[`ssm.StringParameter`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ssm.StringParameter.html)|Returns an instance of ssm.StringParameter created by the construct|
|vpc?|[`ec2.IVpc`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.IVpc.html)|Returns an interface on the VPC used by the pattern (if any). This may be a VPC created by the pattern or the VPC supplied to the pattern constructor.|

## Default settings

Out of the box implementation of the Construct without any override will set the following defaults:

### AWS Lambda Function

* Configure limited privilege access IAM role for Lambda function
* Enable reusing connections with Keep-Alive for NodeJs Lambda function
* Enable X-Ray Tracing
* Set Environment Variables

  * (default) SSM_STRING_PARAMETER_NAME
  * AWS_NODEJS_CONNECTION_REUSE_ENABLED (for Node 10.x and higher functions)

### Amazon AWS Systems Manager Parameter Store String

* Enable read-only access for the associated AWS Lambda Function
* Creates a new SSM String parameter with the values provided
* Retain the SSM String parameter when deleting the CloudFormation stack

## Architecture

![Architecture Diagram](architecture.png)

---


© Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import aws_cdk.aws_ec2 as _aws_cdk_aws_ec2_ceddda9d
import aws_cdk.aws_lambda as _aws_cdk_aws_lambda_ceddda9d
import aws_cdk.aws_ssm as _aws_cdk_aws_ssm_ceddda9d
import constructs as _constructs_77d1e7e8


class LambdaToSsmstringparameter(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-solutions-constructs/aws-lambda-ssmstringparameter.LambdaToSsmstringparameter",
):
    '''
    :summary: The LambdaToSsmstringparameter class.
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        deploy_vpc: typing.Optional[builtins.bool] = None,
        existing_lambda_obj: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.Function] = None,
        existing_string_parameter_obj: typing.Optional[_aws_cdk_aws_ssm_ceddda9d.StringParameter] = None,
        existing_vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
        lambda_function_props: typing.Optional[typing.Union[_aws_cdk_aws_lambda_ceddda9d.FunctionProps, typing.Dict[builtins.str, typing.Any]]] = None,
        string_parameter_environment_variable_name: typing.Optional[builtins.str] = None,
        string_parameter_permissions: typing.Optional[builtins.str] = None,
        string_parameter_props: typing.Optional[typing.Union[_aws_cdk_aws_ssm_ceddda9d.StringParameterProps, typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_props: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.VpcProps, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: - represents the scope for all the resources.
        :param id: - this is a a scope-unique id.
        :param deploy_vpc: Whether to deploy a new VPC. Default: - false
        :param existing_lambda_obj: Existing instance of Lambda Function object, if this is set then the lambdaFunctionProps is ignored. Default: - None
        :param existing_string_parameter_obj: Existing instance of SSM String parameter object, If this is set then the stringParameterProps is ignored. Default: - Default props are used
        :param existing_vpc: An existing VPC for the construct to use (construct will NOT create a new VPC in this case).
        :param lambda_function_props: User provided props to override the default props for the Lambda function. Default: - Default properties are used.
        :param string_parameter_environment_variable_name: Optional Name for the Lambda function environment variable set to the name of the parameter. Default: - SSM_STRING_PARAMETER_NAME
        :param string_parameter_permissions: Optional SSM String parameter permissions to grant to the Lambda function. One of the following may be specified: "Read", "ReadWrite". Default: - Read access is given to the Lambda function if no value is specified.
        :param string_parameter_props: Optional user provided props to override the default props for SSM String parameter. If existingStringParameterObj is not set stringParameterProps is required. The only supported string parameter type is ParameterType.STRING. Default: - Default props are used
        :param vpc_props: Properties to override default properties if deployVpc is true.

        :access: public
        :since: 1.49.0
        :summary: Constructs a new instance of the LambdaToSsmstringparameter class.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ebcad0ac1d88b9a92aae1a25b9fdca6eb528ce9d4060030745abe96dbab7532)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = LambdaToSsmstringparameterProps(
            deploy_vpc=deploy_vpc,
            existing_lambda_obj=existing_lambda_obj,
            existing_string_parameter_obj=existing_string_parameter_obj,
            existing_vpc=existing_vpc,
            lambda_function_props=lambda_function_props,
            string_parameter_environment_variable_name=string_parameter_environment_variable_name,
            string_parameter_permissions=string_parameter_permissions,
            string_parameter_props=string_parameter_props,
            vpc_props=vpc_props,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="lambdaFunction")
    def lambda_function(self) -> _aws_cdk_aws_lambda_ceddda9d.Function:
        return typing.cast(_aws_cdk_aws_lambda_ceddda9d.Function, jsii.get(self, "lambdaFunction"))

    @builtins.property
    @jsii.member(jsii_name="stringParameter")
    def string_parameter(self) -> _aws_cdk_aws_ssm_ceddda9d.StringParameter:
        return typing.cast(_aws_cdk_aws_ssm_ceddda9d.StringParameter, jsii.get(self, "stringParameter"))

    @builtins.property
    @jsii.member(jsii_name="vpc")
    def vpc(self) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc]:
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc], jsii.get(self, "vpc"))


@jsii.data_type(
    jsii_type="@aws-solutions-constructs/aws-lambda-ssmstringparameter.LambdaToSsmstringparameterProps",
    jsii_struct_bases=[],
    name_mapping={
        "deploy_vpc": "deployVpc",
        "existing_lambda_obj": "existingLambdaObj",
        "existing_string_parameter_obj": "existingStringParameterObj",
        "existing_vpc": "existingVpc",
        "lambda_function_props": "lambdaFunctionProps",
        "string_parameter_environment_variable_name": "stringParameterEnvironmentVariableName",
        "string_parameter_permissions": "stringParameterPermissions",
        "string_parameter_props": "stringParameterProps",
        "vpc_props": "vpcProps",
    },
)
class LambdaToSsmstringparameterProps:
    def __init__(
        self,
        *,
        deploy_vpc: typing.Optional[builtins.bool] = None,
        existing_lambda_obj: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.Function] = None,
        existing_string_parameter_obj: typing.Optional[_aws_cdk_aws_ssm_ceddda9d.StringParameter] = None,
        existing_vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
        lambda_function_props: typing.Optional[typing.Union[_aws_cdk_aws_lambda_ceddda9d.FunctionProps, typing.Dict[builtins.str, typing.Any]]] = None,
        string_parameter_environment_variable_name: typing.Optional[builtins.str] = None,
        string_parameter_permissions: typing.Optional[builtins.str] = None,
        string_parameter_props: typing.Optional[typing.Union[_aws_cdk_aws_ssm_ceddda9d.StringParameterProps, typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_props: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.VpcProps, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param deploy_vpc: Whether to deploy a new VPC. Default: - false
        :param existing_lambda_obj: Existing instance of Lambda Function object, if this is set then the lambdaFunctionProps is ignored. Default: - None
        :param existing_string_parameter_obj: Existing instance of SSM String parameter object, If this is set then the stringParameterProps is ignored. Default: - Default props are used
        :param existing_vpc: An existing VPC for the construct to use (construct will NOT create a new VPC in this case).
        :param lambda_function_props: User provided props to override the default props for the Lambda function. Default: - Default properties are used.
        :param string_parameter_environment_variable_name: Optional Name for the Lambda function environment variable set to the name of the parameter. Default: - SSM_STRING_PARAMETER_NAME
        :param string_parameter_permissions: Optional SSM String parameter permissions to grant to the Lambda function. One of the following may be specified: "Read", "ReadWrite". Default: - Read access is given to the Lambda function if no value is specified.
        :param string_parameter_props: Optional user provided props to override the default props for SSM String parameter. If existingStringParameterObj is not set stringParameterProps is required. The only supported string parameter type is ParameterType.STRING. Default: - Default props are used
        :param vpc_props: Properties to override default properties if deployVpc is true.

        :summary: The properties for the LambdaToSsmstringparameter class.
        '''
        if isinstance(lambda_function_props, dict):
            lambda_function_props = _aws_cdk_aws_lambda_ceddda9d.FunctionProps(**lambda_function_props)
        if isinstance(string_parameter_props, dict):
            string_parameter_props = _aws_cdk_aws_ssm_ceddda9d.StringParameterProps(**string_parameter_props)
        if isinstance(vpc_props, dict):
            vpc_props = _aws_cdk_aws_ec2_ceddda9d.VpcProps(**vpc_props)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0284e7e9a7e7884683c6a673d1b61083b6e209f033213143058af7fefac8e2f)
            check_type(argname="argument deploy_vpc", value=deploy_vpc, expected_type=type_hints["deploy_vpc"])
            check_type(argname="argument existing_lambda_obj", value=existing_lambda_obj, expected_type=type_hints["existing_lambda_obj"])
            check_type(argname="argument existing_string_parameter_obj", value=existing_string_parameter_obj, expected_type=type_hints["existing_string_parameter_obj"])
            check_type(argname="argument existing_vpc", value=existing_vpc, expected_type=type_hints["existing_vpc"])
            check_type(argname="argument lambda_function_props", value=lambda_function_props, expected_type=type_hints["lambda_function_props"])
            check_type(argname="argument string_parameter_environment_variable_name", value=string_parameter_environment_variable_name, expected_type=type_hints["string_parameter_environment_variable_name"])
            check_type(argname="argument string_parameter_permissions", value=string_parameter_permissions, expected_type=type_hints["string_parameter_permissions"])
            check_type(argname="argument string_parameter_props", value=string_parameter_props, expected_type=type_hints["string_parameter_props"])
            check_type(argname="argument vpc_props", value=vpc_props, expected_type=type_hints["vpc_props"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if deploy_vpc is not None:
            self._values["deploy_vpc"] = deploy_vpc
        if existing_lambda_obj is not None:
            self._values["existing_lambda_obj"] = existing_lambda_obj
        if existing_string_parameter_obj is not None:
            self._values["existing_string_parameter_obj"] = existing_string_parameter_obj
        if existing_vpc is not None:
            self._values["existing_vpc"] = existing_vpc
        if lambda_function_props is not None:
            self._values["lambda_function_props"] = lambda_function_props
        if string_parameter_environment_variable_name is not None:
            self._values["string_parameter_environment_variable_name"] = string_parameter_environment_variable_name
        if string_parameter_permissions is not None:
            self._values["string_parameter_permissions"] = string_parameter_permissions
        if string_parameter_props is not None:
            self._values["string_parameter_props"] = string_parameter_props
        if vpc_props is not None:
            self._values["vpc_props"] = vpc_props

    @builtins.property
    def deploy_vpc(self) -> typing.Optional[builtins.bool]:
        '''Whether to deploy a new VPC.

        :default: - false
        '''
        result = self._values.get("deploy_vpc")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def existing_lambda_obj(
        self,
    ) -> typing.Optional[_aws_cdk_aws_lambda_ceddda9d.Function]:
        '''Existing instance of Lambda Function object, if this is set then the lambdaFunctionProps is ignored.

        :default: - None
        '''
        result = self._values.get("existing_lambda_obj")
        return typing.cast(typing.Optional[_aws_cdk_aws_lambda_ceddda9d.Function], result)

    @builtins.property
    def existing_string_parameter_obj(
        self,
    ) -> typing.Optional[_aws_cdk_aws_ssm_ceddda9d.StringParameter]:
        '''Existing instance of SSM String parameter object, If this is set then the stringParameterProps is ignored.

        :default: - Default props are used
        '''
        result = self._values.get("existing_string_parameter_obj")
        return typing.cast(typing.Optional[_aws_cdk_aws_ssm_ceddda9d.StringParameter], result)

    @builtins.property
    def existing_vpc(self) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc]:
        '''An existing VPC for the construct to use (construct will NOT create a new VPC in this case).'''
        result = self._values.get("existing_vpc")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc], result)

    @builtins.property
    def lambda_function_props(
        self,
    ) -> typing.Optional[_aws_cdk_aws_lambda_ceddda9d.FunctionProps]:
        '''User provided props to override the default props for the Lambda function.

        :default: - Default properties are used.
        '''
        result = self._values.get("lambda_function_props")
        return typing.cast(typing.Optional[_aws_cdk_aws_lambda_ceddda9d.FunctionProps], result)

    @builtins.property
    def string_parameter_environment_variable_name(
        self,
    ) -> typing.Optional[builtins.str]:
        '''Optional Name for the Lambda function environment variable set to the name of the parameter.

        :default: - SSM_STRING_PARAMETER_NAME
        '''
        result = self._values.get("string_parameter_environment_variable_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def string_parameter_permissions(self) -> typing.Optional[builtins.str]:
        '''Optional SSM String parameter permissions to grant to the Lambda function.

        One of the following may be specified: "Read", "ReadWrite".

        :default: - Read access is given to the Lambda function if no value is specified.
        '''
        result = self._values.get("string_parameter_permissions")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def string_parameter_props(
        self,
    ) -> typing.Optional[_aws_cdk_aws_ssm_ceddda9d.StringParameterProps]:
        '''Optional user provided props to override the default props for SSM String parameter.

        If existingStringParameterObj
        is not set stringParameterProps is required. The only supported string parameter type is ParameterType.STRING.

        :default: - Default props are used
        '''
        result = self._values.get("string_parameter_props")
        return typing.cast(typing.Optional[_aws_cdk_aws_ssm_ceddda9d.StringParameterProps], result)

    @builtins.property
    def vpc_props(self) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.VpcProps]:
        '''Properties to override default properties if deployVpc is true.'''
        result = self._values.get("vpc_props")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.VpcProps], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaToSsmstringparameterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "LambdaToSsmstringparameter",
    "LambdaToSsmstringparameterProps",
]

publication.publish()

def _typecheckingstub__4ebcad0ac1d88b9a92aae1a25b9fdca6eb528ce9d4060030745abe96dbab7532(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    deploy_vpc: typing.Optional[builtins.bool] = None,
    existing_lambda_obj: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.Function] = None,
    existing_string_parameter_obj: typing.Optional[_aws_cdk_aws_ssm_ceddda9d.StringParameter] = None,
    existing_vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
    lambda_function_props: typing.Optional[typing.Union[_aws_cdk_aws_lambda_ceddda9d.FunctionProps, typing.Dict[builtins.str, typing.Any]]] = None,
    string_parameter_environment_variable_name: typing.Optional[builtins.str] = None,
    string_parameter_permissions: typing.Optional[builtins.str] = None,
    string_parameter_props: typing.Optional[typing.Union[_aws_cdk_aws_ssm_ceddda9d.StringParameterProps, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc_props: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.VpcProps, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0284e7e9a7e7884683c6a673d1b61083b6e209f033213143058af7fefac8e2f(
    *,
    deploy_vpc: typing.Optional[builtins.bool] = None,
    existing_lambda_obj: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.Function] = None,
    existing_string_parameter_obj: typing.Optional[_aws_cdk_aws_ssm_ceddda9d.StringParameter] = None,
    existing_vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
    lambda_function_props: typing.Optional[typing.Union[_aws_cdk_aws_lambda_ceddda9d.FunctionProps, typing.Dict[builtins.str, typing.Any]]] = None,
    string_parameter_environment_variable_name: typing.Optional[builtins.str] = None,
    string_parameter_permissions: typing.Optional[builtins.str] = None,
    string_parameter_props: typing.Optional[typing.Union[_aws_cdk_aws_ssm_ceddda9d.StringParameterProps, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc_props: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.VpcProps, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass
