# configues nginx on Ubuntu machine

exec {'update system':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['update system'],
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

exec { 'redirect_me':
  command  => 'sed -i "24i\     rewrite ^/redirect_me https://www.youtube.com/watch?v=TGUlwu4 permanent;" /etc/nginx/sites-available/default',
  provider => 'shell',
}

service {'nginx':
  ensure  => running,
  require => Package['nginx'],
}
