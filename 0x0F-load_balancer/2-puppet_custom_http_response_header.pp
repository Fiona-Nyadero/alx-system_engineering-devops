# 2-puppet_custom_http_response_header.pp

# Installing Nginx
package { 'nginx':
  ensure => installed,
}

# Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
server {
    listen      80 default_server;
    listen      [::]:80 default_server;

    root        /var/www/html;
    index       index.html index.htm;

    server_name _;

    location / {
        add_header X-Served-By $hostname;
        return 200 'Hello World!\\n';
    }
}
",
  require => Package['nginx'],
}

# Symbolic link to enable the site
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}

# Restart Nginx
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
