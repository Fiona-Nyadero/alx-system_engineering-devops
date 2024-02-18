# Puppet fix for a typo error on a wordpress site

# Server returns error 500 cause of .phpp error

exec {'fix_phpp-error':
  command => "sed -i 's/phpp/php/g' '/var/www/html/wp-settings.php'",
  path    => ['/bin','/usr/bin']
}
