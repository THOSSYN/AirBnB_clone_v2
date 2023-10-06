# A puppet manifest to create a web root directory
# Ensure Nginx is installed
package { 'nginx':
  ensure => installed,
}

file { '/data':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
  recurse => true,
}

file { [
  '/data/web_static',
  '/data/web_static/releases',
  '/data/web_static/shared',
  '/data/web_static/releases/test',
]:
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
  recurse => true,
}

file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
  content => content => '<html>
    <head>
    </head>
    <body>
      Holberton School
    </body>
  </html>', 
}

file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  force  => true,
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/data/web_static/current'],
}
