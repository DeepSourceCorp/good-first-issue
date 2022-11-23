---
title: Solidity Cheatsheet
description: Solidity is a statically-typed curly-braces programming language designed for developing smart contracts that run on Ethereum.
created: 2022-10-01
updated: 2022-10-01
---

Solidity is an object-oriented, high-level language for implementing smart contracts. Smart contracts are programs which govern the behaviour of accounts within the Ethereum state.

## Basic Contract using Solidity

```
// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.16 <0.9.0;

contract SimpleStorage {
    uint storedData;

    function set(uint x) public {
        storedData = x;
    }

    function get() public view returns (uint) {
        return storedData;
    }
}
```

### Pragma

```
pragma solidity ^{version};
pragma solidity ^0.4.25;
```
---

## Import Files

`import "filename";`

`import * as symbolName from "filename";` or `import "filename" as symbolName;`

`import {symbol1 as alias, symbol2} from "filename";`

## Data Types

`type [public] [constant] name;`
`uint public amount;`
`delete amount;` - deletes variable content

Getters are automatically generated for public vars. constant vars have to be initialized on declaration.

### Boolean

`bool` : `true` or `false`

Operators:

- Logical : `!` (logical negation), `&&` (AND), `||` (OR)
- Comparisons : `==` (equality), `!=` (inequality)

### Integer

Unsigned : `uint8 | uint16 | uint32 | uint64 | uint128 | uint256(uint)`

Signed   : `int8  | int16  | int32  | int64  | int128  | int256(int) `

Operators:

- Comparisons: `<=`, `<`, `==`, `!=`, `>=` and `>`
- Bit operators: `&`, `|`, `^` (bitwise exclusive or) and `~` (bitwise negation)
- Arithmetic operators: `+`, `-`, unary `-`, unary `+`, `*`, `/`, `%`, `**` (exponentiation), `<<` (left shift) and `>>` (right shift)

### Address

`address`: Holds an Ethereum address (20 byte value).
`address payable` : Same as address, but includes additional methods `transfer` and `send`

Operators:

- Comparisons: `<=`, `<`, `==`, `!=`, `>=` and `>`

Methods:

#### balance

- `<address>.balance (uint256)`: balance of the Address in Wei

#### transfer and send

- `<address>.transfer(uint256 amount)`: send given amount of Wei to Address, throws on failure
- `<address>.send(uint256 amount) returns (bool)`: send given amount of Wei to Address, returns false on failure

#### call
- `<address>.call(...) returns (bool)`: issue low-level CALL, returns false on failure

#### delegatecall

- `<address>.delegatecall(...) returns (bool)`: issue low-level DELEGATECALL, returns false on failure.

#### callcode
- `<address>.callcode(...) returns (bool)`: issue low-level CALLCODE, returns false on failure

## Control Structures

Most of the control structures from JavaScript are available in Solidity except for `switch` and `goto`. 

- `if` `else`
- `while`
- `do`
- `for`
- `break`
- `continue`
- `return`
- `? :`

### Flow Control

`if (condition) { ... };`
`if (condition) { ... } else { ... };`
`for (declaration; condition; expression) { ... };`

`while (condition) { ... };`
`do { ... } while (condition);`
`condition ? expression : expression;`

> continue, break and return can be used to influence flow.

### Array

Arrays can be dynamic or have a fixed size.

```solidity
uint[] dynamicSizeArray;

uint[7] fixedSizeArray;
```

`myArray[3]; - get element`
`myArray[3] = 8; - set element`
`uint[] memory myArray = new uint[](5);` 
> memory array with size determined at runtime. Memory arrays can't have dynamic size

### Fixed byte arrays

`bytes1(byte)`, `bytes2`, `bytes3`, ..., `bytes32`.

Operators:

Comparisons: `<=`, `<`, `==`, `!=`, `>=`, `>` (evaluate to bool)
Bit operators: `&`, `|`, `^` (bitwise exclusive or), `~` (bitwise negation), `<<` (left shift), `>>` (right shift)
Index access: If x is of type bytesI, then x[k] for 0 <= k < I returns the k th byte (read-only).

Members

- `.length` : read-only

### Dynamic byte arrays

`bytes`: Dynamically-sized `byte` array. It is similar to `byte[]`, but it is packed tightly in calldata. Not a value-type!

`string`: Dynamically-sized UTF-8-encoded string. It is equal to `bytes` but does not allow length or index access. Not a value-type!

### Enum

Enum works just like in every other language.

```solidity
enum ActionChoices { 
  GoLeft, 
  GoRight, 
  GoStraight, 
  SitStill 
}

ActionChoices choice = ActionChoices.GoStraight;
```

### Struct

New types can be declared using struct.

```solidity
struct Funder {
    address addr;
    uint amount;
}

Funder funders;
```

### Mapping

Declared as `mapping(_KeyType => _ValueType)`

Mappings can be seen as **hash tables** which are virtually initialized such that every possible key exists and is mapped to a value.

**key** can be almost any type except for a mapping, a dynamically sized array, a contract, an enum, or a struct. **value** can actually be any type, including mappings.

> All possible mapping keys always exists and have a default byte value of all zeroes. Can't be iterated, checked for length, retrieve which keys were set etc. Also can't be created in memory.

---

## Functions

### Structure

`function (<parameter types>) {internal|external|public|private} [pure|constant|view|payable] [returns (<return types>)]`

### Access modifiers

- ```public``` - Accessible from this contract, inherited contracts and externally
- ```private``` - Accessible only from this contract
- ```internal``` - Accessible only from this contract and contracts inheriting from it
- ```external``` - Cannot be accessed internally, only externally. Recommended to reduce gas. Access internally with `this.f`.

### Parameters

#### Input parameters

Parameters are declared just like variables and are `memory` variables.

```solidity
function f(uint _a, uint _b) {}
```

#### Output parameters

Output parameters are declared after the `returns` keyword

```solidity
function f(uint _a, uint _b) returns (uint _sum) {
   _sum = _a + _b;
}
```

Output can also be specified using `return` statement. In that case, we can omit parameter name `returns (uint)`.

Multiple return types are possible with `return (v0, v1, ..., vn)`.


### Constructor

Function that is executed during contract deployment. Defined using the `constructor` keyword.

```solidity
contract C {
   address owner;
   uint status;
   constructor(uint _status) {
       owner = msg.sender;
       status = _status;
   }
}
```

### Function Calls

#### Internal Function Calls

Functions of the current contract can be called directly (internally - via jumps) and also recursively

```solidity
contract C {
    function funA() returns (uint) { 
       return 5; 
    }
    
    function FunB(uint _a) returns (uint ret) { 
       return funA() + _a; 
    }
}
```

#### External Function Calls

`this.g(8);` and `c.g(2);` (where c is a contract instance) are also valid function calls, but, the function will be called “externally”, via a message call.

> `.gas()` and `.value()` can also be used with external function calls.

#### Named Calls

Function call arguments can also be given by name in any order as below.

```solidity
function f(uint a, uint b) {  }

function g() {
    f({b: 1, a: 2});
}
```

#### Unnamed function parameters

Parameters will be present on the stack, but are not accessible.

```solidity
function f(uint a, uint) returns (uint) {
    return a;
}
```

### Function Modifier

Modifiers can automatically check a condition prior to executing the function.

```solidity
modifier onlyOwner {
    require(msg.sender == owner);
    _;
}

function close() onlyOwner {
    selfdestruct(owner);
}
```

### Function type

Pass function as a parameter to another function. Similar to `callbacks` and `delegates`

```solidity
pragma solidity ^0.4.18;

contract Oracle {
  struct Request {
    bytes data;
    function(bytes memory) external callback;
  }
  Request[] requests;
  event NewRequest(uint);
  function query(bytes data, function(bytes memory) external callback) {
    requests.push(Request(data, callback));
    NewRequest(requests.length - 1);
  }
  function reply(uint requestID, bytes response) {
    // Here goes the check that the reply comes from a trusted source
    requests[requestID].callback(response);
  }
}

contract OracleUser {
  Oracle constant oracle = Oracle(0x1234567); // known contract
  function buySomething() {
    oracle.query("USD", this.oracleResponse);
  }
  function oracleResponse(bytes response) {
    require(msg.sender == address(oracle));
  }
}
```

### Pure Functions

Functions can be declared `pure` in which case they promise not to read from or modify the state.

```solidity
function f(uint a) pure returns (uint) {
    return a * 42;
}
```

### Payable Functions

Functions that receive `Ether` are marked as `payable` function.

### Fallback Function

A contract can have exactly one **unnamed function**. This function cannot have arguments and cannot return anything. It is executed on a call to the contract if none of the other functions match the given function identifier (or if no data was supplied at all).

```solidity
function() {
  // Do something
}
```


### Mathematical and Cryptographic Functions

- `addmod(uint x, uint y, uint k) returns (uint)`:
   compute (x + y) % k where the addition is performed with arbitrary precision and does not wrap around at 2**256.
- `mulmod(uint x, uint y, uint k) returns (uint)`:
   compute (x * y) % k where the multiplication is performed with arbitrary precision and does not wrap around at 2**256.
- `sha3(...) returns (bytes32)`:
   alias to keccak256
- `ripemd160(...) returns (bytes20)`:
   compute RIPEMD-160 hash of the (tightly packed) arguments
- `keccak256(...) returns (bytes32)`:
   compute the Ethereum-SHA-3 (Keccak-256) hash of the (tightly packed) arguments
- `sha256(...) returns (bytes32)`:
   compute the SHA-256 hash of the (tightly packed) arguments

---

## Interface

`Interfaces` are similar to abstract contracts, but they have restrictions:

- Cannot have any functions implemented.
- Cannot inherit other contracts or interfaces.
- Cannot define constructor.
- Cannot define variables.
- Cannot define structs.
- Cannot define enums.

> Interfaces are like abstract contracts which other contracts can inherit. Inheriting contract has to implement all interface methods. Interfaces can't contain anything else than function signatures.

```solidity
pragma solidity ^0.4.11;

interface Token {
    function transfer(address recipient, uint amount);
}
```

---

## Contracts

### Creating contracts using `new`

Contracts can be created from another contract using `new` keyword. The source of the contract has to be known in advance.

```solidity
contract A {
    function add(uint _a, uint _b) returns (uint) {
        return _a + _b;
    }
}

contract C {
    address a;
    function f(uint _a) {
        a = new A();
    }
}
```

### Contract Inheritance

Solidity supports multiple inheritance and polymorphism.

```solidity
contract owned {
    function owned() { owner = msg.sender; }
    address owner;
}

contract mortal is owned {
    function kill() {
        if (msg.sender == owner) selfdestruct(owner);
    }
}

contract final is mortal {
    function kill() { 
        super.kill(); // Calls kill() of mortal.
    }
}
```

##### Example

`Memo memo = new Memo("my precious memo");` - create new contract
`Memo memo = Memo(existingMemoAddress);` - intialize already existing contract
`this;` - current contract
`address(this);` - converts contract to address
`selfdestruct(ownerAddress);` - destroys contract and sends it's funds to address. Must be called from contract.

#### Constructor of base class

```solidity
contract A {
    uint a;
    constructor(uint _a) { a = _a; }
}

contract B is A(1) {
    constructor(uint _b) A(_b) {
    }
}
```

### Abstract Contracts

Contracts that contain implemented and non-implemented functions. Such contracts cannot be compiled, but they can be used as base contracts.

```solidity
pragma solidity ^0.4.0;

contract A {
    function C() returns (bytes32);
}

contract B is A {
    function C() returns (bytes32) { return "c"; }
}
```
---

## Deprecations

`constant` - function modifier
`year` - time literal suffix
`throw` - alias to revert
`block.blockhash(block_number);` - replaced by global blockhash(block_number);
`msg.gas` - replaced by global gasleft();
`suicide` - alias to selfdestruct(address)
`keccak256(a, b)` - deprecated in favor ofkeccak256(abi.encodePacked(a, b))



## Events

Events allow the convenient usage of the EVM logging facilities, which in turn can be used to “call” JavaScript callbacks in the user interface of a dapp, which listen for these events.

Up to three parameters can receive the attribute indexed, which will cause the respective arguments to be searched for.

> All non-indexed arguments will be stored in the data part of the log.

```solidity
pragma solidity ^0.4.0;

contract ClientReceipt {
    event Deposit(
        address indexed _from,
        bytes32 indexed _id,
        uint _value
    );

    function deposit(bytes32 _id) payable {
        emit Deposit(msg.sender, _id, msg.value);
    }
}
```


## Library

Libraries are similar to contracts, but they are deployed only once at a specific address, and their code is used with [`delegatecall`](#delegatecall) (`callcode`). 

```solidity
library arithmatic {
    function add(uint _a, uint _b) returns (uint) {
        return _a + _b;
    }
}

contract C {
    uint sum;

    function f() {
        sum = arithmatic.add(2, 3);
    }
}
```

## Error Handling

- `assert(bool condition)`: throws if the condition is not met - to be used for internal errors.
- `require(bool condition)`: throws if the condition is not met - to be used for errors in inputs or external components.
- `revert()`: abort execution and revert state changes

```solidity
 function sendHalf(address addr) payable returns (uint balance) {
    require(msg.value % 2 == 0); // Only allow even numbers
    uint balanceBeforeTransfer = this.balance;
    addr.transfer(msg.value / 2);
    assert(this.balance == balanceBeforeTransfer - msg.value / 2);
    return this.balance;
}
```

---

## Variables

### Transaction variables

- `msg.data (bytes)`: complete calldata
- `msg.gas (uint)`: remaining gas
- `msg.sender (address)`: sender of the message (current call)
- `msg.sig (bytes4)`: first four bytes of the calldata (i.e. function identifier)
- `msg.value (uint)`: number of wei sent with the message
- `tx.gasprice (uint)`: gas price of the transaction
- `tx.origin (address)`: sender of the transaction (full call chain)


### Block variables

- `block.blockhash(uint blockNumber) returns (bytes32)`: hash of the given block - only works for the 256 most recent blocks excluding current
- `block.coinbase (address)`: current block miner’s address
- `block.difficulty (uint)`: current block difficulty
- `block.gaslimit (uint)`: current block gaslimit
- `block.number (uint)`: current block number
- `block.timestamp (uint)`: current block timestamp as seconds since unix epoch
- `now (uint)`: current block timestamp (alias for `block.timestamp`)


Here is an image cheatsheet for quick recall. [Image](https://intellipaat.com/mediaFiles/2019/03/Solidity-Cheat-Sheet.jpg)
