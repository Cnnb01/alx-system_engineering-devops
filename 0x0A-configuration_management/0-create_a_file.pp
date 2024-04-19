# Creating a file

$str = 'I love Puppet'

file {'/tmp/school':
    ensure  => present,
    content => $str,
    group => 'www-data',
    mode => '0744',
    owner => 'www-data',
}