#include <stdio.h>
#include <time.h>
#include <unistd.h>

int main() {
  while (1) {
    time_t current_time;
    time(&current_time);
    struct tm *time_info = localtime(&current_time);
    printf("%02d:%02d:%02d\n", time_info->tm_hour, time_info->tm_min, time_info->tm_sec);
    sleep(1);
  }
  return 0;
}

