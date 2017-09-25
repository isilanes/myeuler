clc
clear all

tic
nmax = 100000000;
listprimes = primes(nmax);


listtest = 1:nmax;
listvalid = {};

div = 0;
prog = nmax;
while length(listtest)>0
    
    div = div + 1;
    divisibles = listtest(rem(listtest, div)==0);
    
    if isempty(divisibles)
        continue
    end
    
    listBAD = setdiff(divisibles, div*(listprimes-div));
    listOK = listtest(listtest<div.^2);
    
    listvalid{end+1} = listOK;
    listtest = setdiff(listtest,[listBAD listOK]);

end

sprintf('%i', sum([listvalid{:}]))
toc
