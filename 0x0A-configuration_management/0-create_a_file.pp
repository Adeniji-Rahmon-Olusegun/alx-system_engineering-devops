# creates a file in /tmp

file { '/tmpschool':
  content => 'I love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}
