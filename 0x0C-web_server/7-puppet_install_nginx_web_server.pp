# Nginx server config

package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure => running,
  enable => true,
  require => Package['nginx'],
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "# Nginx server block\n
              server {\n
                listen 80 default_server;\n
                listen [::]:80 default_server;\n\n
                root /var/www/html;\n
                index index.html index.htm;\n\n
                server_name _;\n\n
                default_type text/html;\n\n
                location / {\n
                  return 200 'Hello World!\\n';\n
                }\n\n
                location /redirect_me {\n
                  return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n
                }\n\n
                error_page 404 /404_custom_page;\n
                location = /404_custom_page {\n
                  internal;\n
                  return 404 'Ceci n''est pas une page\\n';\n
                }\n
              }",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
  notify  => Service['nginx'],
}
