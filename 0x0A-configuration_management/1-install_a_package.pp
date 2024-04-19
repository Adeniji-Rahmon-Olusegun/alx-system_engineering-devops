# installs flask from pip3

package { 'flask':
  ensure   => installed,
  name     => 'python3-flask',
  provider => 'pip3',
  require  => Package['python3'],
  ensure_version => '== 2.1.0',
}
