#Install package

exec {'sudo gem install flask -v 2.1.0':
    path => ['/usr/bin'],
}
