### Improved Flag Checker

See solver.py for angr script.

Output:

λ time python solver2.py
WARNING | 2021-08-27 14:22:58,306 | cle.loader | The main binary is a position-independent executable. It is being loaded with a base address of 0x400000.
WARNING | 2021-08-27 14:22:59,162 | angr.simos.simos | stdin is constrained to 32 bytes (has_end=True). If you are only providing the first 32 bytes instead of the entire stdin, please use stdin=SimFileStream(name='stdin', content=your_first_n_bytes, has_end=False).
b'BHCTF21"""!0""$0(0$((($00$!(0!!\n'
b'BHCTF21{1(0(!@!$(!+!((!"y@"!!$!\n'
b'BHCTF21{g0($"$(""("!!"!""0"("0!\n'
b'BHCTF21{gd0$"("(!0$@$"$$$0((((!\n'
b'BHCTF21{gdb$($!0"0!0((!!0$((("!\n'
b'BHCTF21{gdb_p!00""$$$"@$("$"0(!\n'
b'BHCTF21{gdb_00$0(($("0!(!?0"0$!\n'
b'BHCTF21{gdb_0r""!!0("!"!(?!$0(!\n'
b'BHCTF21{gdb_0r_!0"0!"("$0$(!$!!\n'
b'BHCTF21{gdb_0r_gb00"00"("((0!(!\n'
b'BHCTF21{gdb_0r_gh0(0"!0(!"("(0!\n'
b'BHCTF21{gdb_0r_gh1(0!0("!(0!"(!\n'
b'BHCTF21{gdb_0r_gh1d0($0!0$!$!0!\n'
b'BHCTF21{gdb_0r_gh1dr$(@0"?00($!\n'
b'BHCTF21{gdb_0r_gh1dra("00?!!"0!\n'
b'BHCTF21{gdb_0r_gh1dra_!00?0!00!\n'
b'BHCTF21{gdb_0r_gh1dra_1"!?@$(0!\n'
b'BHCTF21{gdb_0r_gh1dra_1_g?0@!!!\n'
b'BHCTF21{gdb_0r_gh1dra_1_w&"((0!\n'
b'BHCTF21{gdb_0r_gh1dra_1_w0p?!$!\n'
b'BHCTF21{gdb_0r_gh1dra_1_w0nb$"!\n'
b'BHCTF21{gdb_0r_gh1dra_1_w0nd}$!\n'
b'BHCTF21{gdb_0r_gh1dra_1_w0ndr}!\n'
b'BHCTF21{gdb_0r_gh1dra_1_w0ndrd!\n'
python solver2.py  17.23s user 0.45s system 90% cpu 19.506 total

Flag is: BHCTF21{gdb_0r_gh1dra_1_w0ndr}
