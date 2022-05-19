import psutil
      
for part in psutil.disk_partitions(all=True):
    #print(part)
    try:
        disk_usage = (psutil.disk_usage)(part.mountpoint)
    except Exception as e:
        print(
            u'Unable to get disk metrics for {}: {}. '
            u'You can exclude this mountpoint in the settings if it is invalid.'.format(
            part.mountpoint,
            e)
        )
        continue