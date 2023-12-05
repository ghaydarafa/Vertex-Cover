from vertex_cover_dp import run_and_measure as run_dp
from vertex_cover_bnb import run_and_measure as run_bnb

def main():
    run_dp('./dataset/small_dp.graph')
    run_dp('./dataset/medium_dp.graph')
    run_dp('./dataset/large_dp.graph')

    run_bnb('./dataset/small_bnb.graph')
    run_bnb('./dataset/medium_bnb.graph')
    run_bnb('./dataset/large_bnb.graph')

if __name__ == "__main__":
    main()
