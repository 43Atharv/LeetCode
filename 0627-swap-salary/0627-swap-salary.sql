update salary SET sex=
CASE sex
    when 'm' then 'f'
    when 'f' then 'm'
    ELSE 'm'
    end;
    