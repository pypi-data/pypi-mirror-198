import argparse
from .jskiner import InferenceEngine


def run() -> None:
    parser = argparse.ArgumentParser(
        description='Inferencing Json Schema')

    parser.add_argument('--jsonl',
                        type=str, required=True,
                        help="Inference Json Schema from .jsonl file")

    parser.add_argument('--nworkers',
                        type=int, required=False, default=1,
                        help="Inference Worker Count")

    parser.add_argument('--verbose',
                        type=bool, required=False, default=False,
                        help="Showing the Result by Pretty Print")

    parser.add_argument('--out',
                        type=str, required=False, default='',
                        help="Saving the json schema into a output file")

    args = parser.parse_args()
    print(f"Your json file is at: {args.jsonl}")
    print('verbose:', args.verbose)

    with open(args.jsonl, 'r') as f:
        json_list = [x for x in f]

    engine = InferenceEngine(args.nworkers)
    schema_str = engine.run(json_list)
    if args.verbose:
        print(schema_str)
    if args.out != '':
        with open(args.out, 'w') as f:
            f.write(schema_str)
