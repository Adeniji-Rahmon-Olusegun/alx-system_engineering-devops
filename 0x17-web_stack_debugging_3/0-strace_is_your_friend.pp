# Fix 500 error on Apache

exec { 'fix-error`':
  command => '/bin/sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => 'var/www/html/wp-settings.php',
}
