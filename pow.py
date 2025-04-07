import hashlib

def compute_hash(input_str):
    return hashlib.sha256(input_str.encode()).hexdigest()

def proof_of_work(client_id, target_prefix, params):
    n = 0
    
    while True:
        combined = f"{client_id}:{n}:{','.join(params)}"
        hash_result = compute_hash(combined)
        
        if hash_result.startswith(target_prefix):
            print(f"Valid PoW Found! Nonce: {n}")
            return n
        
        n += 1

if __name__ == "__main__":
    client_id = "AW0ZZ1dvBZbRgWbGw_RH1SvdeV-q2Z6YHcC2Hte-bT8MA2zVSfFGuH0aAkLBb-wiCbsl3oirSUlQdJGJHpOc7waULIw_AvoJ2j16jkzlhxRBZl3k3lCJH0DiG0GSNoNVrw==" #session id
    target_prefix = "000"
    params = [
        'sq0idp-wGVapF8sNt9PLrdj5znuKA',  # client id
        'LCSA1H88XBAFS',                  # location id
        'e93f344b-24e8-4f67-9e4b-eb60e2fd98e3' # instance id
    ]
    nonce = proof_of_work(client_id, target_prefix, params)