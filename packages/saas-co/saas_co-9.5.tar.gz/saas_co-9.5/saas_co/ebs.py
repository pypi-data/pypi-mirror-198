from .cw import get_metrics

#####################################

def get_ebs_metrics(**kargs):

    kargs['query'] = [
        ("AWS/EC2", "EBSReadBytes",  "Sum", "Bytes", False, "ebs_read_bytes"),
        ("AWS/EC2", "EBSWriteBytes",  "Sum", "Bytes", False, "ebs_write_bytes")
    ]
    return cs.get_metrics(kargs) 

#####################################