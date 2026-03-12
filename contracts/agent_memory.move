module memory_network::agent_memory {

    use std::string::String;
    use std::signer;
    use aptos_framework::timestamp;

    const ENOT_OWNER: u64 = 1;

    struct MemoryPointer has key {
        shelby_url: String,
        owner: address,
        last_updated: u64,
        read_price: u64
    }

    public entry fun initialize_agent(
        account: &signer,
        initial_url: String,
        price: u64
    ) {

        let addr = signer::address_of(account);

        move_to(account, MemoryPointer {
            shelby_url: initial_url,
            owner: addr,
            last_updated: timestamp::now_seconds(),
            read_price: price
        });
    }

    public entry fun update_memory(
        account: &signer,
        new_url: String
    ) acquires MemoryPointer {

        let addr = signer::address_of(account);
        let pointer = borrow_global_mut<MemoryPointer>(addr);

        assert!(pointer.owner == addr, ENOT_OWNER);

        pointer.shelby_url = new_url;
        pointer.last_updated = timestamp::now_seconds();
    }

    public fun get_memory(agent: address): (String, u64, u64) acquires MemoryPointer {

        let pointer = borrow_global<MemoryPointer>(agent);

        (
            pointer.shelby_url,
            pointer.last_updated,
            pointer.read_price
        )
    }
}
