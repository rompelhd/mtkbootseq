# mtkbootseq
mtkbootseq is a lightweight Python utility that communicates with the MediaTek (MTK) Preloader over its serial interface during the early boot process. It sends a predefined boot sequence to request a specific boot mode, such as FASTBOOT, META, or Factory Mode, provided the device's preloader supports it.

Acknowledgements

Special thanks to all the companies that have spent years turning device ownership into a privilege instead of a right.

Without locked bootloaders, missing fastboot implementations, mandatory online accounts, arbitrary waiting periods, vendor-specific unlock tools, region locks, and undocumented boot protocols... projects like this probably wouldn't exist.

🍅 Just terrible!

Manufacturers that have made unlocking impossible on many or all of their devices without unofficial workarounds:

Alcatel
Amazon
Apple
Asus
Cat
Coolpad
Doogee
Energizer
Huawei
Meizu
Panasonic
Samsung
Sharp
TCL / BlackBerry
Vivo / iQOO
Vsmart
Windows Phone vendors

⛔ Avoid at all costs!

Manufacturers that only allow unlocking under specific conditions (region, model, SoC, carrier...) or require unnecessary sacrifices:

Hisense
HMD / Nokia
Honor
HTC
LG
Motorola / Lenovo / NEC
OPPO / Realme
Oukitel
Xiaomi / Redmi / POCO
ZTE / nubia / RedMagic

⚠️ Proceed with caution!

Manufacturers that require an online account, approval process, waiting period, or other unnecessary hurdles:

Fairphone
Google / Nexus
Infinix
itel
OnePlus
Sony
Tecno
And finally...

A special mention to Google, for steadily making Android modification more difficult through increasingly strict security mechanisms, stronger hardware attestation, tighter Verified Boot integration, and an ecosystem that makes rooting and custom ROM development more challenging with every release.

Owning a device should mean owning it—not renting permission to use hardware you already paid for.

Fuck you all 