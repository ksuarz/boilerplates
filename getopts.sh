OPTIND=1

while getopts "abcd" opt; do
    case "$opt" in
        *)
            echo "Unrecognized option: -$opt"
            exit 1
            ;;
    esac
done
shift $((OPTIND-1))
