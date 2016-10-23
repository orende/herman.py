import md5

secret = 'e1862debf36ed3d9eabef0d5c456d53a'
guess = '1'

if md5.new(guess).hexdigest() == secret:
    print 'Found correct string'

# Berätta vilket tal mellan 1 till 1000000000 som skapade md5-strängen sparad i variabeln secret
