from jsonpath_ng import parse
from .paginate import ec2_paginate

#####################################

class describe_regions(ec2_paginate):
    def name(self): return __class__.__name__        
    def jsonpath_expression(self): return parse('Regions[*]')

#####################################

class describe_instances(ec2_paginate):
    def name(self): return __class__.__name__        
    def jsonpath_expression(self): return parse('Reservations[*].Instances[*]')

#####################################

class describe_vpc_endpoints(ec2_paginate):
    def name(self): return __class__.__name__
    def jsonpath_expression(self): return parse('VpcEndpoints[*]')

#####################################

class describe_nat_gateways(ec2_paginate):
    def name(self): return __class__.__name__
    def jsonpath_expression(self): return parse('NatGateways[*]')

#####################################

class describe_subnets(ec2_paginate):
    def name(self): return __class__.__name__
    def jsonpath_expression(self): return parse('Subnets[*]')

#####################################

class describe_route_tables(ec2_paginate):
    def name(self): return __class__.__name__
    def jsonpath_expression(self): return parse('RouteTables[*]')

#####################################

class describe_prefix_lists(ec2_paginate):
    def name(self): return __class__.__name__
    def jsonpath_expression(self): return parse('PrefixLists[*]')

#####################################

class describe_vpcs(ec2_paginate):
    def name(self): return __class__.__name__
    def jsonpath_expression(self): return parse('Vpcs[*]')

#####################################

class describe_instance_types(ec2_paginate):
    def name(self): return __class__.__name__
    def jsonpath_expression(self): return parse('InstanceTypes[*]')

#####################################

class describe_launch_templates(ec2_paginate):
    def name(self): return __class__.__name__
    def jsonpath_expression(self): return parse('LaunchTemplates[*]')

#####################################

class describe_launch_template_versions(ec2_paginate):
    def name(self): return __class__.__name__
    def jsonpath_expression(self): return parse('LaunchTemplateVersions[*]')

#####################################

import boto3
import datetime as dt  
from itertools import groupby
from datetime import datetime, timedelta

def get_cpu_util_metrics(**kargs):
    
    client = kargs.get('session').client('cloudwatch')
    iid = kargs.get('instance_id')
    days = kargs.get('days',31)
    period = kargs.get('period',300)
    dimensions = [{"Name": "InstanceId", "Value": iid}]

    dimensions = [{"Name": "InstanceId", "Value": instance_id}]
    queries = [
        {
            "Id": "cpu_util", 
            "MetricStat": {
                "Metric": {
                    "Namespace": "AWS/EC2", 
                    "MetricName": "CPUUtilization", 
                    "Dimensions": dimensions
                },                
                "Period": period,                
                "Stat": "Maximum"
            },            
            "Label": "cpu_util_max",        
        },
        {
            "Id": "cpu_util", 
            "MetricStat": {
                "Metric": {
                    "Namespace": "AWS/EC2", 
                    "MetricName": "CPUUtilization", 
                    "Dimensions": dimensions
                },                
                "Period": period,                
                "Stat": "SampleCount"
            },            
            "Label": "cpu_util_count",        
        },

    ]
    
    results = client.get_metric_data(
        MetricDataQueries=queries,
        StartTime = dt.datetime.today() - timedelta(days=days + 1),
        EndTime=dt.datetime.today() - timedelta(days=1),
    )["MetricDataResults"]
    
    return {k: list(group) for k, group in groupby(results, key=lambda r: r["Label"])}

#####################################

