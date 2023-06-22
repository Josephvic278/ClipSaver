import urllib.parse
import requests

parsed_url = urllib.parse.urlparse('https://www.youtube.com/watch?v=O0HQnTJhr70')
print(parsed_url)
# Check if the scheme is http or https and if the netloc ends with youtube.com or youtu.be
if parsed_url.scheme in ('http', 'https') and parsed_url.netloc.endswith(('youtube.com', 'youtu.be')):
	# Split the netloc into subcomponents
	split_netloc = urllib.parse.urlsplit(parsed_url.netloc)
	# Check if the hostname ends with sv and if yes, replace it with clipsaver.com
	if split_netloc.hostname.endswith('sv'):
		new_hostname = split_netloc.hostname[:-2] + 'clipsaver.com'
		# Reassemble the netloc with the new hostname
		new_netloc = urllib.parse.urlunsplit((split_netloc.username, split_netloc.password, new_hostname, split_netloc.port, None))
		# Reassemble the URL with the new netloc
		new_url = urllib.parse.urlunparse((parsed_url.scheme, new_netloc, parsed_url.path, parsed_url.params, parsed_url.query, parsed_url.fragment))
		# Return the modified URL
		print( new_url)
	else:
		# Return None if the hostname does not end with sv
		print( None)
else:
# Return None if the scheme is not http or https or if the netloc does not end with youtube.com or youtu.be
	print( None)

modified_url = modify_url('https://www.youtube.com/watch?v=O0HQnTJhr70')
print(modified_url)



"""Collecting environment information...
PyTorch version: 2.0.1+cu118
Is debug build: False
CUDA used to build PyTorch: 11.8
ROCM used to build PyTorch: N/A

OS: Ubuntu 20.04.6 LTS (x86_64)
GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0
Clang version: 10.0.0-4ubuntu1 
CMake version: version 3.25.2
Libc version: glibc-2.31

Python version: 3.10.12 (main, Jun  7 2023, 12:45:35) [GCC 9.4.0] (64-bit runtime)
Python platform: Linux-5.15.107+-x86_64-with-glibc2.31
Is CUDA available: True
CUDA runtime version: 11.8.89
CUDA_MODULE_LOADING set to: LAZY
GPU models and configuration: GPU 0: Tesla T4
Nvidia driver version: 525.85.12
cuDNN version: Probably one of the following:
/usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.0
/usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.0
/usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.0
/usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.0
/usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.9.0
/usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.9.0
/usr/lib/x86_64-linux-gnu/libcudnn_ops_train.so.8.9.0
HIP runtime version: N/A
MIOpen runtime version: N/A
Is XNNPACK available: True

CPU:
Architecture:                    x86_64
CPU op-mode(s):                  32-bit, 64-bit
Byte Order:                      Little Endian
Address sizes:                   46 bits physical, 48 bits virtual
CPU(s):                          2
On-line CPU(s) list:             0,1
Thread(s) per core:              2
Core(s) per socket:              1
Socket(s):                       1
NUMA node(s):                    1
Vendor ID:                       GenuineIntel
CPU family:                      6
Model:                           85
Model name:                      Intel(R) Xeon(R) CPU @ 2.00GHz
Stepping:                        3
CPU MHz:                         2000.152
BogoMIPS:                        4000.30
Hypervisor vendor:               KVM
Virtualization type:             full
L1d cache:                       32 KiB
L1i cache:                       32 KiB
L2 cache:                        1 MiB
L3 cache:                        38.5 MiB
NUMA node0 CPU(s):               0,1
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Mitigation; PTE Inversion
Vulnerability Mds:               Vulnerable; SMT Host state unknown
Vulnerability Meltdown:          Vulnerable
Vulnerability Mmio stale data:   Vulnerable
Vulnerability Retbleed:          Vulnerable
Vulnerability Spec store bypass: Vulnerable
Vulnerability Spectre v1:        Vulnerable: __user pointer sanitization and usercopy barriers only; no swapgs barriers
Vulnerability Spectre v2:        Vulnerable, IBPB: disabled, STIBP: disabled, PBRSB-eIBRS: Not affected
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Vulnerable
Flags:                           fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc rep_good nopl xtopology nonstop_tsc cpuid tsc_known_freq pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch invpcid_single ssbd ibrs ibpb stibp fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm mpx avx512f avx512dq rdseed adx smap clflushopt clwb avx512cd avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves arat md_clear arch_capabilities

Versions of relevant libraries:
[pip3] numpy==1.22.4
[pip3] pytorch3d==0.7.4
[pip3] torch==2.0.1+cu118
[pip3] torchaudio==2.0.2+cu118
[pip3] torchdata==0.6.1
[pip3] torchsummary==1.5.1
[pip3] torchtext==0.15.2
[pip3] torchvision==0.15.2+cu118
[conda] Could not collect

"""