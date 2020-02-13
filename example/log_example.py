import standard_log as log
import time


log.status("Doing some stuff ...")

for i in range(10):
	log.spinner("Doing it ",i,speed=1.)
	time.sleep(.2)

log.success("Did a bunch of stuff")
log.advisory("Stuff already done, you are good to go.")
log.warning("Not that stuff, need to do the other stuff.")
log.error("Oops too late, can't do it anymore.",error=True)

