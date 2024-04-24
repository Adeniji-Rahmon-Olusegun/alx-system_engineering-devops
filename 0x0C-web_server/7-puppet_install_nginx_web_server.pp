# installs nginx on ubuntu using puppet

package { 'nginx':
  ensure => installed,
}

service { 'nginx'
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx],
}

server {
    listen 80 default_server;
    listen [::]: default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    location / {
        try_files $uri $uri/ =404;
    }

    location = /redirect_me {
	return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    location = / {
        return 200 "Hello World!\n";
    }
}
