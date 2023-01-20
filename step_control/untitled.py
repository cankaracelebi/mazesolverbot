import machine
import time

# When the following number is sampled at four consecutive
# even-numbered bits it will have two bits set, but sampling at four
# consecutive odd-numbered bits will only yield one bit set.

_WAVE_MAGIC = 0b0000011100000111

class Stepper:
    def __init__(self, A, B, C, D, T=1):
        if not isinstance(T, machine.Timer):
            T = machine.Timer(T)
        self._timer = T
        l = []
        for p in (A, B, C, D):
            if not isinstance(p, machine.Pin):
                p = machine.Pin(p, machine.Pin.OUT)
            l.append(p)
        self._pins = l
        self._phase = 0
        self._stop()
        self._run_remaining = 0

    def _stop(self):
        [p.off() for p in self._pins]

    # Note: This is called on an interrupt on some platforms, so it must not use the heap
    def _callback(self, t):
        if self._run_remaining != 0:
            direction = 1 if self._run_remaining > 0 else -1
            self._phase = (self._phase + direction) % 8
            wave = _WAVE_MAGIC >> self._phase
            for i in range(4):
                self._pins[i].value((wave >> (i*2)) & 1)
            self._run_remaining -= direction
        else:
            self._timer.deinit()
            self._stop()

    def run(self, count, delay=0.001):
        tick_hz=1000000
        period = int(delay*tick_hz)
        if period < 500:
            period = 500
        self._run_remaining += count
        if self._run_remaining != 0:
            self._timer.init(period=period, tick_hz=tick_hz,
                             mode=machine.Timer.PERIODIC, callback=self._callback)
        else:
            self._timer.deinit()
            self._stop()

    def stop(self):
        remaining = self._run_remaining
        self._run_remaining = 0
        self._timer.deinit()
        self._stop()
        return remaining

    @property
    def is_running(self):
        return self._run_remaining != 0