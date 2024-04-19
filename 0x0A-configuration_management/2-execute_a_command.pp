# Creating a manifest that kills a process
exec{ 'killmenow':
    commannd => 'pkill killmenow',
    path    => '/usr/bin/'
}