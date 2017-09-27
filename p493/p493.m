tic
situations = 10*ones(1,7); % balls
probs = 1;

for i = 1:20
    newsits = [];
    newprobs = [];

    for isit = 1:size(situations,1)
        situation = situations(isit,:);
        prob = probs(isit); 
        
        newsits{isit} = sort(repmat(situation,[7,1])-diag(ones(7,1)),2);
        newprobs{isit} = prob*situation'/sum(situation);
        
    end
    newsits = cat(1,newsits{:});
    newprobs = cat(1,newprobs{:});
    
    bads = newprobs<=0;
    if any(bads)
        newsits(bads,:) = [];
        newprobs(bads) = [];
    end
    
    [situations,ia,ic] = unique(newsits,'rows');
    probs = nan(size(situations,1),1);
    for isit = 1:size(situations,1)
        probs(isit) = sum(newprobs(ic==isit));
    end
    
end

ncolors = sum(situations<10,2);
result = sum(probs.*ncolors);

fprintf('%1d\n', ncolors)
fprintf('%1.11f\n', probs)

fprintf('%1.11f\n', result)
toc

% Fractions of n colors:
% 2 0.0000000000
% 3 0.0000000065
% 4 0.0000297769
% 5 0.0060243276
% 6 0.1691201861
% 7 0.8248257029
