import angr
import claripy

p = angr.Project('./improved_flag_checker')

flag_chars = [claripy.BVS('flag_%d' % i, 8) for i in range(31)]
flag = claripy.Concat(*flag_chars + [claripy.BVV(b'\n')])

st = p.factory.full_init_state(
    stdin = flag,
    add_options = angr.options.unicorn,
)

for i in flag_chars:
    st.solver.add(i >= ord('!'))
    st.solver.add(i <= ord('~'))

sm = p.factory.simulation_manager(st)
sm.run()

for i in sm.deadended:
    if b'BHCTF21' in i.posix.dumps(1):
        print(i.posix.dumps(0))

