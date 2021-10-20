#pragma once

#define APP_VERSION "1.2.0.4"

#if defined(ROLE_APP1)
#define APP_NAME "app1.exe"
#elif defined(ROLE_APP2)
#define APP_NAME "app2.exe"
#else
#error
#endif
