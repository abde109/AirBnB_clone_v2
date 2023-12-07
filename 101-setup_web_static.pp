# 101-setup_web_static.pp
class web_static_setup {
    package { 'nginx':
        ensure => installed,
    }

    file { '/data':
        ensure  => directory,
        owner   => 'ubuntu',
        group   => 'ubuntu',
        require => Package['nginx'],
    }

    file { '/data/web_static':
        ensure  => directory,
        require => File['/data'],
    }

    file { '/data/web_static/releases':
        ensure  => directory,
        require => File['/data/web_static'],
    }

    file { '/data/web_static/shared':
        ensure  => directory,
        require => File['/data/web_static'],
    }

    file { '/data/web_static/releases/test':
        ensure  => directory,
        require => File['/data
