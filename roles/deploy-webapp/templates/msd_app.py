import datetime
import psutil
import re

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    sorted_keys = environ.keys()
    sorted_keys.sort()
    host_ip = str(environ['REMOTE_ADDR'])
    octets_list = [int(x) for x in host_ip.split(".")]
    octets_str_unparsed = str(["Even " if i % 2 == 0 else "Odd " for i in octets_list])
    octets_str = str(re.search(r'\[(.*?)\]', octets_str_unparsed).group(1))
    now = datetime.datetime.now()
    current_datetime = now.strftime("%I:%M%p on %B %d, %Y")
    cpu_stats_basic = str(psutil.cpu_percent())
    cpu_stats_detailed_unparsed=str(psutil.cpu_times_percent())
    cpu_stats_detailed = str(re.search(r'\((.*?)\)', cpu_stats_detailed_unparsed).group(1))
    mem_stats_detailed_unparsed = str(psutil.virtual_memory())
    mem_stats_detailed = str(re.search(r'\((.*?)\)', mem_stats_detailed_unparsed).group(1))
    swap_mem_stats_detailed_unparsed = str(psutil.swap_memory())
    swap_mem_stats_detailed = str(re.search(r'\((.*?)\)', swap_mem_stats_detailed_unparsed).group(1))
    partitions_detailed_unparsed = str(psutil.disk_partitions())
    partitions_detailed = str(re.search(r'\((.*?)\)', partitions_detailed_unparsed).group(1))
    root_partition_detailed_unparsed = str(psutil.disk_usage('/'))
    root_partition_detailed = str(re.search(r'\((.*?)\)', root_partition_detailed_unparsed).group(1))
    result = ['<h1>&nbsp;&nbsp;&nbsp;Hello MSD!</h1>'] + \
             ['<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This is demo of WSGI application for getting following system info:</p><p><ul>'] + \
             ['<li><b><i>IP of machine:</i></b> %s </li>' % host_ip] + \
             ['<li><b><i>Octets:</i></b> %s </li>' % octets_str] + \
             ['<li><b><i>Date and time:</i></b> %s </li>' % current_datetime] + \
             ['<li><b><i>CPU usage (total):</i></b> %s' % cpu_stats_basic] + \
             ['<li><b><i>CPU usage (detailed):</i></b> %s </li>' % cpu_stats_detailed] + \
             ['<li><b><i>Memory usage:</i></b> %s </li>' % mem_stats_detailed] +\
             ['<li><b><i>Swap memory usage:</i></b> %s </li>' % swap_mem_stats_detailed] +\
             ['<li><b><i>Partitions:</i></b> %s </li>' % partitions_detailed] +\
             ['<li><b><i>Root partition usage:</i></b> %s </li>' % root_partition_detailed] +\
             ['</ul></p>']
    return result