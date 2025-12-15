# Host-Test.ru benchmark
Host-Test.ru Server Benchmark includes geekbench, speedtest, fio and other

This is simple bash and python scripts based at bench.monster scripts
# Requirements
 - bzip2, wget, fio, python3
 - Run from /root dirrectory is required for speedtest ookla

# Run:
 - curl -LsO http://selcdn.x-api.net/bench/bench.sh; bash bench.sh {option. only one. Example: -bench}
 - curl -LsO https://raw.githubusercontent.com/xakep7/host-test-benchmark/refs/heads/main/bench.sh; bash bench.sh {option. only one. Example: -bench}

# Options
- --info - Show System info
- --version - Show script version
- --geek5 - Run geekbench v5 only
- --ioping - Run io test only
- --geoip - Show GeoIP info
- -a or --a or -all or --all or -bench or --bench or -Global - Run all benchmarks, worldwide speedtest servers and share results
- usa or -usa or --usa or us or -us or --us or USA or -USA or --USA - Run all benchmarks, USA speedtest servers and share results
- europe or -europe or --europe or eu or -eu or --eu or Europe or -Europe or --Europe - Run all benchmarks, Europe speedtest servers and share results
- russia or -russia or --russia or ru or -ru or --ru or Russia or -Russia or --Russia - Run all benchmarks, Russia speedtest servers and share results
- china or -china or --china or mjj or -mjj or cn or -cn or --cn or China or -China or --China - Run all benchmarks, China speedtest servers and share results



Result is shown at https://host-test.ru/dsrating
