# reconfigure nginx to accomodate more traffic

exec { 'maximum limit setting':
  command => 'sed -i "s/5/10000/" /etc/default/nginx && sudo service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
}
