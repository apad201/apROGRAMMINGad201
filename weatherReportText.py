from subprocess import Popen, PIPE

output = Popen(['curl', '-s', 'http://api.wunderground.com/api/6fd4d9217972df59/conditions/q/NC/Durham.xml'], stdout=PIPE)
weatherReport = output.stdout.read()
print weatherReport
