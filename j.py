import jenkins

print(jenkins.__file__)

server = jenkins.Jenkins('http://localhost:8080/jenkins', username='bhenriquea', password='@indra2018')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))
print(server.get_promotions('selenium'))